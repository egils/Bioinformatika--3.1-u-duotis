Bioinformatika,3.1-užduotis
============================

Bioinformatika, Programų sistemų 7 semestro praktinė užduotis, 3.1 atsiskaitomasis darbas

Apie
====
Tai yra bioinformatikos 3.1 uzduoties realizacija,
kuria atliko Egidijus Lukauskas.

Programos kodas parasytas Python (v2.6-7) kalba yra faile "bio.py".

Veikimas
========

Į katalogus "threat" ir "nonthreat" parsiunčiamos sekos ir išsaugomos
failuose, kurių pavadinimai atrodo taip: "hpv_type_XX.fasta".

Tuose pačiuose kataloguose, programos cdhit pagalba, yra sugeneruojami
failai be identiškų sekų. Jų pavadinimai atitinkamai: "hpv_type_xx_unique.fasta".

"merged_seq.fasta" failas yra sugeneruotas paėmus visų *unique* failų
iš katalogų "threat" ir "nonthreat" turinius. Šis failas panaudotas 
sugeneruoti rezultato failui "mafft_aligned.fasta". Jis sugeneruojamas
programos MAFFT pagalba.

Pateikiamas Makefile, kuris eksportuoja mafft programai reikalingą globalu kintamąjį.
Jeigu eksportavimas nereikalingas, programa paleidziama tiesiog komandine eilute 
"python bio.py" (gali kisti priklausomai nuo naudojamos OS).


