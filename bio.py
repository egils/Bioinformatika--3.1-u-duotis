import os
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIStandalone
from Bio.Blast import NCBIXML
from Bio.Alphabet import generic_protein
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio import SeqIO
import textwrap
import subprocess

hpv_threat = [16]
hpv_nonthreat = []

# get blastn results and not valid items
def get_blast_alignments(seq, query):
  ncbi = NCBIWWW.qblast(program="blastn" , database="nr", 
                      sequence=seq, entrez_query=query, format_type="XML", hitlist_size = 500, expect = 100.0)
  blast = NCBIXML.read(ncbi);
  remove_alignments = []
  
  query_length = len(seq);

  #results = []
  #for alignment in blast.alignments:
    #positive = alignment.hsps[0].positives * 100 / 80
    #if positive >= 80:
      #results.append(alignment)
  #return results
  for alignment in blast.alignments:
    overall_length = 0.0
    for hsp in alignment.hsps:
      overall_length += hsp.align_length
    if (overall_length / query_length) < 0.8:
      remove_alignments.append(alignment)

  for alignment in remove_alignments:
    blast.alignments.remove(alignment)
    
  return blast.alignments;

# write aligned sequences
def write_aligned(alignments, filename):
  results = []
  for alignment in alignments:
    results.append(SeqRecord(Seq(alignment.hsps[0].sbjct, generic_protein), id = alignment.title))
  SeqIO.write(results, filename, "fasta")
    
# controller to download sequences
def get_sequences(seq):
  print "Getting threat sequences."
  for nr in hpv_threat:
    query = "*type " + str(nr) + "*[title]"
    print "Executing query: " + query
    alignments = get_blast_alignments(seq, query);
    write_aligned(alignments, "threat/hpv_type_" + str(nr) + ".fasta");
  print "Getting non-threat sequences."
  for nr in hpv_nonthreat:
    query = "*type " + str(nr) + "*[title]"
    print "Executing query: " + query
    alignments = get_blast_alignments(seq, query);
    write_aligned(alignments, "nonthreat/hpv_type_"+str(nr)+".fasta");
    
# controller to remove identical sequence
def remove_identical():
  print "Removeing identical sequences with cd-hit."
  for nr in hpv_threat:
    filename = "threat/hpv_type_" + str(nr)
    print "Working with \""+filename+".fasta\""
    os.system("cdhit -i "+filename+".fasta -o "+filename+"_unique.fasta -c 1 -M 0")
  for nr in hpv_nonthreat:
    filename = "nonthreat/hpv_type_" + str(nr)
    print "Working with \""+filename+".fasta\""
    os.system("cdhit -i "+filename+".fasta -o "+filename+"_unique.fasta -c 1 -M 0")
    
def merge_and_align():
  print "Mergeing fasta files into one \"merged_seq.fasta\""
  files = []
  for nr in hpv_threat:
    files.append("threat/hpv_type_" + str(nr) + "_unique.fasta")
  for nr in hpv_nonthreat:
    files.append("nonthreat/hpv_type_" + str(nr) + "_unique.fasta")
  
  output = open("merged_seq.fasta", "w")
  for filename in files:
    try:
      handler = open(filename, "r")
      sequences = handler.read()
      output.write(sequences + '\n');
      handler.close()
    except IOError as e:
      print "File \"" + filename + "\" could not be read. Maybe cdhit failed on it?"      
    
  output.close()
  
  print "Aligning useing mafft. Output file is \"mafft_aligned.fasta\""
  os.system('mafft --quiet merged_seq.fasta > mafft_aligned.fasta')

    
if __name__ == "__main__":
  seq = SeqIO.read(open("L1seq.fasta"), format="fasta")
  get_sequences(seq.format("fasta"))
  remove_identical()
  merge_and_align()