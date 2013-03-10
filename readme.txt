Tai yra bioinformatikos 3.1 uzduoties realizacija,
kuria atliko Egidijus Lukauskas, PS2.

Programos kodas parasytas python kalba yra faile "bio.py".

I katalogus "threat" ir "nonthreat" parsiunciamos sekos ir issaugomos
failuose, kuri pavadinimai atrodo taip: "hpv_type_XX.fasta".

Tuose paciuose kataloguose, programos cdhit pagalba, yra sugeneruojami
failai be identisku seku. Ju pavadinimai atitinkamai: "hpv_type_xx_unique.fasta".

"merged_seq.fasta" failas yra sugeneruotas paemus visu *unique* failu
is katalogu "threat" ir "nonthreat" turinius. Sis failas panaudotas 
sugeneruoti rezultato failui "mafft_aligned.fasta". Jis sugeneruojamas
programos MAFFT pagalba.

Pridedamas Makefile, kuris eksportuoja mafft programai reikalinga globalu kintamaji.
Jeigu eksportavimas nereikalingas, programa paleidziama tiesiog komandine eilute 
"python bio.py"


