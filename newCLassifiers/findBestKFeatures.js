let featureRanking = [
  245, 238, 244, 108, 64, 78, 107, 250, 233, 248, 251, 247, 249, 62, 256, 3, 117, 39, 75, 115, 19, 76, 172, 41, 70, 61, 236, 164, 54, 17, 65, 257, 77, 224, 143, 31, 66, 254, 167, 48, 20, 253, 154, 33, 30, 179, 72, 94, 110, 93, 109, 79, 83, 95, 80, 27, 9, 35, 7, 23, 14, 24, 47, 49, 86, 44, 46, 113, 45, 69, 237, 37, 1, 240, 58, 59, 213, 38, 60, 55, 185, 29, 88, 205, 22, 111, 4, 229, 53, 90, 96, 21, 112, 89, 208, 56, 106, 207, 36, 255, 52, 144, 16, 178, 133, 15, 252, 74, 190, 42, 188, 81, 18, 246, 87, 222, 43, 84, 101, 1, 68, 34, 241, 40, 239, 97, 129, 130, 120, 137, 135, 134, 198, 142, 98, 193, 173, 103, 194, 125, 119, 209, 126, 136, 116, 182, 161, 235, 128, 180, 67, 73, 189, 186, 150, 201, 102, 138, 169, 191, 192, 177, 176, 196, 226, 140, 217, 149, 132, 231, 131, 123, 124, 105, 104, 234, 166, 163, 162, 216, 168, 232, 230, 145, 174, 212, 228, 227, 200, 199, 211, 114, 220, 181, 203, 204, 206, 221, 153, 171, 214, 202, 147, 148, 127, 210, 151, 175, 139, 118, 218, 141, 99, 100, 195, 155, 170, 215, 165, 152, 219, 258, 197, 26, 32, 50, 187, 157, 223, 225, 2, 25, 92, 122, 121, 5, 156, 146, 91, 13, 51, 57, 28, 6, 183, 158, 1, 159, 11, 184, 242, 243, 63, 71, 10, 12, 8, 82, 85, 160
]

let features = [
  "characterCount", "wordCount", "syllableCount", "sentenceCount", "sectionCount", "subsectionCount", "paragraphCount", "meanSectionSize", "meanParagraphSize", "largestSectionSize", "shortestSectionSize", "largestShortestSectionRatio", "sectionSizeStandardDeviation", "meanOfSubsectionsPerSection", "abstractSize", "abstractSizeArtcileLengthRatio", "citationCount", "citationCountPerTextLength", "citationCountPerSection", "externalLinksCount", "externalLinksPerTextLength", "externalLinksPerSection", "imageCount", "imagePerTextLength", "imagePerSection", "meanSentenceSize", "largestSentenceSize", "shortestSentenceSize", "largeSentenceRate", "shortSentenceRate", "questionCount", "questionRatio", "exclamationCount", "exclamationRatio", "toBeVerbCount", "toBeVerbRatio", "toBeVerbPerSentence", "toBeVerbRate", "modalAuxiliaryVerbCount", "modalAuxiliaryVerbsRatio", "modalAuxiliaryVerbsPerSentence", "modalAuxiliaryVerbsRate", "passiveVoiceCount", "passiveVoiceRatio", "passiveVoicePerSentence", "passiveVoiceRate", "numberOfSentencesThatStartWithACoordinatingConjunction", "numberOfSentencesThatStartWithADeterminer", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction", "numberOfSentencesThatStartWithAnAdjective", "numberOfSentencesThatStartWithANoun", "numberOfSentencesThatStartWithAPronoun", "numberOfSentencesThatStartWithAnAdverb", "numberOfSentencesThatStartWithAnArticle", "numberOfSentencesThatStartWithACoordinatingConjunctionRatio", "numberOfSentencesThatStartWithADeterminerRatio", "numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunctionRatio", "numberOfSentencesThatStartWithAnAdjectiveRatio", "numberOfSentencesThatStartWithANounRatio", "numberOfSentencesThatStartWithAPronounRatio", "numberOfSentencesThatStartWithAnAdverbRatio", "numberOfSentencesThatStartWithAnArticleRatio", "automatedReadabilityIndex", "colemanLiauIndex", "fleshReadingEase", "fleschKincaidGradeLevel", "gunningFogIndex", "lasbarhetsIndex", "smogGrading", "daleChallReadabilityFormula", "differentWordCount", "differentWordsPerSentence", "differentWordsRate", "nounCount", "nounsPerSentence", "nounsRate", "differentNounCount", "differentNounsPerSentence", "differentNounsRate", "differentNounsDifferentWordsRatio", "verbCount", "verbsPerSentence", "verbsRate", "differentVerbCount", "differentVerbsPerSentence", "differentVerbsRate", "differentVerbsDifferentWordsRatio", "pronounCount", "pronounsPerSentence", "pronounsRate", "differentPronounCount", "differentPronounsPerSentence", "differentPronounsRate", "differentPronounsDifferentWordsRatio", "adjectiveCount", "adjectivesPerSentence", "adjectivesRate", "differentAdjectiveCount", "differentAdjectivesPerSentence", "differentAdjectivesRate", "differentAdjectivesDifferentWordsRatio", "adverbCount", "adverbsPerSentence", "adverbsRate", "differentAdverbCount", "differentAdverbsPerSentence", "differentAdverbsRate", "differentAdverbsDifferentWordsRatio", "coordinatingConjunctionCount", "coordinatingConjunctionsPerSentence", "coordinatingConjunctionsRate", "differentCoordinatingConjunctionCount", "differentCoordinatingConjunctionsPerSentence", "differentCoordinatingConjunctionsRate", "differentCoordinatingConjunctionsDifferentWordsRatio", "subordinatingPrepositionAndConjunctionCount", "subordinatingPrepositionsAndConjunctionsPerSentence", "subordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionAndConjunctionCount", "differentSubordinatingPrepositionsAndConjunctionsPerSentence", "differentSubordinatingPrepositionsAndConjunctionsRate", "differentSubordinatingPrepositionsAndConjunctionsDifferentWordsRatio", "syllablesPerWord", "charactersPerWord", "NNP,NNP,NNP", "VBD,DT,JJ", "IN,DT,NNP", "NNP,IN,DT", "DT,NNP,NNP", "JJ,NN,IN", "NN,IN,DT", "IN,DT,NN", "NN,IN,NNP", "IN,NNP,NNP", "NNP,VBD,DT", "VBD,DT,NN", "DT,NN,IN", "VBD,VBN,IN", "NNP,NNP,VBD", "IN,NN,IN", "NNP,NNP,IN", "NNP,IN,NNP", "VBD,IN,DT", "IN,DT,JJ", "JJ,NNS,IN", "DT,JJ,NN", "IN,DT,NNS", "IN,CD,NNP", "VBN,IN,DT", "DT,NN,NN", "IN,PRP$,NN", "NNP,VBD,VBN", "NNP,CC,NNP", "NNS,IN,DT", "NN,IN,NN", "DT,NN,VBD", "NN,VBD,VBN", "TO,VB,DT", "NNP,POS,NN", "ter", "er_", "_wa", "was", "as_", "s_a", "_a_", "an_", "e_a", "_an", "and", "nd_", "_re", "ent", "_of", "of_", "f_t", "_th", "the", "he_", "on_", ",_a", "at_", "ed_", "_on", "n_t", "or_", "ing", "ng_", "_in", "in_", "d_t", "d_a", "_he", "_to", "ted", "th_", "al_", "es_", "ate", "_co", "ion", "ere", "_fo", "for", "s,_", "to_", "ati", "st_", "re_", "_be", "ly_", "her", "_hi", "his", "is_", "e_t", "en_", "e_o", "t_t", "tio", "_Th", "age", "agePerReview", "reviewPerDay", "reviewsPerUser", "reviewsPerUserStdDev", "discussionCount", "reviewCount", "registeredReviewCount", "anonymouseReviewCount", "registeredReviewRate", "anonymouseReviewRate", "registeredAnonymouseReviewRatio", "userCount", "occasionalUserCount", "occasionalUserRate", "registeredUserCount", "anonymouseUserCount", "registerdAnonymouseUserRatio", "registeredUserRate", "anonymouseUserRate", "revertCount", "revertReviewRatio", "diversity", "modifiedLinesRate", "mostActiveUsersReviewCount", "mostActiveUsersReviewRate", "lastThreeMonthsReviewCount", "lastThreeMonthsReviewRate", "pageRank", "indegree", "outdegree", "assortativity_inin", "assortativity_inout", "assortativity_outin", "assortativity_outout", "localClusteringCoefficient", "reciprocity", "linkCount", "translationCount"
]

// console.log(features[featureRanking.indexOf(1)])
// console.log(features[featureRanking.indexOf(2)])
// console.log(features[featureRanking.indexOf(3)])
// console.log(features[featureRanking.indexOf(4)])
// console.log(features[featureRanking.indexOf(5)])
// console.log(features[featureRanking.indexOf(6)])
// console.log(features[featureRanking.indexOf(7)])
// console.log(features[featureRanking.indexOf(8)])
// console.log(features[featureRanking.indexOf(9)])
// console.log(features[featureRanking.indexOf(10)])
// console.log(features[featureRanking.indexOf(11)])
// console.log(features[featureRanking.indexOf(12)])
// console.log(features[featureRanking.indexOf(13)])
// console.log(features[featureRanking.indexOf(14)])
// console.log(features[featureRanking.indexOf(15)])
// console.log(features[featureRanking.indexOf(16)])
// console.log(features[featureRanking.indexOf(17)])
// console.log(features[featureRanking.indexOf(18)])
// console.log(features[featureRanking.indexOf(19)])
// console.log(features[featureRanking.indexOf(20)])
// console.log(features[featureRanking.indexOf(21)])
// console.log(features[featureRanking.indexOf(22)])
// console.log(features[featureRanking.indexOf(23)])
// console.log(features[featureRanking.indexOf(24)])
// console.log(features[featureRanking.indexOf(25)])
// console.log(features[featureRanking.indexOf(26)])
// console.log(features[featureRanking.indexOf(27)])
// console.log(features[featureRanking.indexOf(28)])
// console.log(features[featureRanking.indexOf(29)])
// console.log(features[featureRanking.indexOf(30)])
// console.log(features[featureRanking.indexOf(31)])
// console.log(features[featureRanking.indexOf(32)])
// console.log(features[featureRanking.indexOf(33)])
// console.log(features[featureRanking.indexOf(34)])
// console.log(features[featureRanking.indexOf(35)])
// console.log(features[featureRanking.indexOf(36)])
// console.log(features[featureRanking.indexOf(37)])
// console.log(features[featureRanking.indexOf(38)])
// console.log(features[featureRanking.indexOf(39)])
// console.log(features[featureRanking.indexOf(40)])
// console.log(features[featureRanking.indexOf(41)])
// console.log(features[featureRanking.indexOf(42)])
// console.log(features[featureRanking.indexOf(43)])
// console.log(features[featureRanking.indexOf(44)])
// console.log(features[featureRanking.indexOf(45)])
// console.log(features[featureRanking.indexOf(46)])
// console.log(features[featureRanking.indexOf(47)])
// console.log(features[featureRanking.indexOf(48)])
// console.log(features[featureRanking.indexOf(49)])
// console.log(features[featureRanking.indexOf(50)])
// console.log(features[featureRanking.indexOf(51)])
// console.log(features[featureRanking.indexOf(52)])
// console.log(features[featureRanking.indexOf(53)])
// console.log(features[featureRanking.indexOf(54)])
// console.log(features[featureRanking.indexOf(55)])
// console.log(features[featureRanking.indexOf(56)])
// console.log(features[featureRanking.indexOf(57)])
// console.log(features[featureRanking.indexOf(58)])
// console.log(features[featureRanking.indexOf(59)])
// console.log(features[featureRanking.indexOf(60)])
// console.log(features[featureRanking.indexOf(61)])
// console.log(features[featureRanking.indexOf(62)])
// console.log(features[featureRanking.indexOf(63)])
// console.log(features[featureRanking.indexOf(64)])
// console.log(features[featureRanking.indexOf(65)])
// console.log(features[featureRanking.indexOf(66)])
// console.log(features[featureRanking.indexOf(67)])
// console.log(features[featureRanking.indexOf(68)])
// console.log(features[featureRanking.indexOf(69)])
// console.log(features[featureRanking.indexOf(70)])



let a = [0.31892857142857145, 0.3457142857142857, 0.36214285714285716, 0.37785714285714284, 0.36892857142857144, 0.40107142857142858, 0.40928571428571431, 0.41857142857142859, 0.42392857142857143, 0.42607142857142855, 0.43821428571428572, 0.45607142857142857, 0.47642857142857142, 0.47107142857142859, 0.47749999999999998, 0.48321428571428571, 0.48035714285714287, 0.49249999999999999, 0.48428571428571426, 0.48785714285714288, 0.48678571428571427, 0.49249999999999999, 0.495, 0.49321428571428572, 0.49178571428571427, 0.49821428571428572, 0.49071428571428571, 0.49464285714285716, 0.49357142857142855, 0.50071428571428567, 0.49249999999999999, 0.49785714285714283, 0.49678571428571427, 0.50392857142857139, 0.50214285714285711, 0.50321428571428573, 0.5089285714285714, 0.50571428571428567, 0.53821428571428576, 0.53142857142857147, 0.53249999999999997, 0.5357142857142857, 0.53357142857142859, 0.53678571428571431, 0.53178571428571431, 0.54249999999999998, 0.53428571428571425, 0.53928571428571426, 0.53821428571428576, 0.54785714285714282, 0.54107142857142854, 0.54107142857142854, 0.53642857142857148, 0.54285714285714282, 0.53607142857142853, 0.53428571428571425, 0.53892857142857142, 0.5446428571428571, 0.53428571428571425, 0.53857142857142859, 0.54214285714285715, 0.5407142857142857, 0.53964285714285709, 0.53749999999999998, 0.54428571428571426, 0.54357142857142859, 0.53428571428571425, 0.5346428571428572, 0.54035714285714287, 0.53607142857142853, 0.53714285714285714, 0.53857142857142859, 0.54249999999999998, 0.54035714285714287, 0.53821428571428576, 0.5357142857142857, 0.53642857142857148, 0.5357142857142857, 0.54357142857142859, 0.53642857142857148, 0.54535714285714287, 0.53964285714285709, 0.53892857142857142, 0.54535714285714287, 0.54249999999999998, 0.53928571428571426, 0.54321428571428576, 0.53857142857142859, 0.53678571428571431, 0.54249999999999998, 0.53964285714285709, 0.53714285714285714, 0.53928571428571426, 0.54035714285714287, 0.53964285714285709, 0.54142857142857148, 0.5346428571428572, 0.53821428571428576, 0.54000000000000004, 0.54428571428571426, 0.54000000000000004, 0.53714285714285714, 0.54535714285714287, 0.54178571428571431, 0.53500000000000003, 0.54892857142857143, 0.53607142857142853, 0.54785714285714282, 0.54000000000000004, 0.54535714285714287, 0.54607142857142854, 0.55285714285714282, 0.5535714285714286, 0.54678571428571432, 0.54642857142857137, 0.54249999999999998, 0.54642857142857137, 0.53785714285714281, 0.54357142857142859, 0.54749999999999999, 0.53749999999999998, 0.55000000000000004, 0.54107142857142854, 0.54535714285714287, 0.54678571428571432, 0.5496428571428571, 0.5446428571428571, 0.55321428571428577, 0.5446428571428571, 0.54642857142857137, 0.55285714285714282, 0.55714285714285716, 0.55321428571428577, 0.54749999999999999, 0.55107142857142855, 0.55214285714285716, 0.55285714285714282, 0.54642857142857137, 0.54571428571428571, 0.54607142857142854, 0.54321428571428576, 0.5485714285714286, 0.54821428571428577, 0.54714285714285715, 0.55178571428571432, 0.55321428571428577, 0.55178571428571432, 0.5575, 0.55285714285714282, 0.55178571428571432, 0.5546428571428571, 0.56071428571428572, 0.56071428571428572, 0.55857142857142861, 0.5675, 0.56714285714285717, 0.56178571428571433, 0.56071428571428572, 0.55821428571428566, 0.5625, 0.56428571428571428, 0.56464285714285711, 0.56999999999999995, 0.55785714285714283, 0.55857142857142861, 0.5625, 0.56785714285714284, 0.56571428571428573, 0.5625, 0.55607142857142855, 0.56535714285714289, 0.56535714285714289, 0.5675, 0.56071428571428572, 0.56321428571428567, 0.56499999999999995, 0.55964285714285711, 0.56285714285714283, 0.56499999999999995, 0.56178571428571433, 0.56464285714285711, 0.55928571428571427, 0.56000000000000005, 0.56571428571428573, 0.56714285714285717, 0.56678571428571434, 0.56071428571428572, 0.55678571428571433, 0.5625, 0.56857142857142862, 0.55785714285714283, 0.55571428571428572, 0.55964285714285711, 0.56035714285714289, 0.5675, 0.56178571428571433, 0.56678571428571434, 0.56571428571428573, 0.5625, 0.56321428571428567, 0.56071428571428572, 0.56607142857142856, 0.56178571428571433, 0.56392857142857145, 0.56142857142857139, 0.56357142857142861, 0.55857142857142861, 0.56857142857142862, 0.56428571428571428, 0.56285714285714283, 0.56214285714285717, 0.56464285714285711, 0.55678571428571433, 0.56214285714285717, 0.56107142857142855, 0.56678571428571434, 0.56357142857142861, 0.56499999999999995, 0.55964285714285711, 0.55821428571428566, 0.56071428571428572, 0.56107142857142855, 0.56499999999999995, 0.56464285714285711, 0.56285714285714283, 0.56392857142857145, 0.5625, 0.56678571428571434, 0.56392857142857145, 0.56678571428571434, 0.56499999999999995, 0.56214285714285717, 0.56357142857142861, 0.56000000000000005, 0.56714285714285717, 0.56642857142857139, 0.56678571428571434, 0.56642857142857139, 0.56071428571428572, 0.55857142857142861, 0.5625, 0.55821428571428566, 0.55964285714285711, 0.5625, 0.55892857142857144, 0.55428571428571427, 0.56571428571428573, 0.55785714285714283]

let max = 0

a.forEach((n) => {
  if (n > max) {
    max = n
  }
})

console.log(a.indexOf(max));
console.log(a[a.indexOf(max)] + 1);




// characterCount
// wordCount
// syllableCount
// sentenceCount
// sectionCount
// subsectionCount
// paragraphCount
// meanSectionSize
// meanParagraphSize
// largestSectionSize
// shortestSectionSize
// largestShortestSectionRatio
// sectionSizeStandardDeviation
// meanOfSubsectionsPerSection
// abstractSize
// abstractSizeArtcileLengthRatio
// citationCount
// citationCountPerSection
// externalLinksCount
// externalLinksPerSection
// imageCount
// imagePerSection
// largestSentenceSize
// shortestSentenceSize
// toBeVerbCount
// modalAuxiliaryVerbCount
// passiveVoiceCount
// numberOfSentencesThatStartWithADeterminer
// numberOfSentencesThatStartWithASubordinatingPrepositionOrConjunction
// numberOfSentencesThatStartWithAnAdjective
// numberOfSentencesThatStartWithANoun
// numberOfSentencesThatStartWithAPronoun
// numberOfSentencesThatStartWithAnAdverb
// numberOfSentencesThatStartWithAnArticle
// differentWordCount
// differentWordsPerSentence
// nounCount
// differentNounCount
// differentNounsPerSentence
// verbCount
// differentVerbCount
// pronounCount
// differentPronounCount
// adjectiveCount
// differentAdjectiveCount
// adverbCount
// differentAdverbCount
// coordinatingConjunctionCount
// differentCoordinatingConjunctionCount
// subordinatingPrepositionAndConjunctionCount
// differentSubordinatingPrepositionAndConjunctionCount
// differentSubordinatingPrepositionsAndConjunctionsPerSentence
// NNP,NNP,NNP
// VBD,DT,JJ
// IN,DT,NNP
// NNP,IN,DT
// DT,NNP,NNP
// JJ,NN,IN
// NN,IN,DT
// IN,DT,NN
// NN,IN,NNP
// IN,NNP,NNP
// NNP,VBD,DT
// VBD,DT,NN
// DT,NN,IN
// VBD,VBN,IN
// NNP,NNP,VBD
// IN,NN,IN
// NNP,NNP,IN
// NNP,IN,NNP
// VBD,IN,DT
// IN,DT,JJ
// JJ,NNS,IN
// DT,JJ,NN
// IN,DT,NNS
// IN,CD,NNP
// VBN,IN,DT
// DT,NN,NN
// IN,PRP$,NN
// NNP,VBD,VBN
// NNP,CC,NNP
// NNS,IN,DT
// NN,IN,NN
// DT,NN,VBD
// NN,VBD,VBN
// TO,VB,DT
// NNP,POS,NN
// ter
// er_
// _wa
// was
// as_
// s_a
// _a_
// an_
// e_a
// _an
// and
// nd_
// _re
// ent
// _of
// of_
// f_t
// _th
// the
// he_
// on_
// ,_a
// at_
// ed_
// _on
// n_t
// or_
// ing
// ng_
// _in
// in_
// d_t
// d_a
// _he
// _to
// ted
// th_
// al_
// es_
// ate
// _co
// ion
// ere
// _fo
// for
// s,_
// to_
// ati
// st_
// re_
// _be
// ly_
// her
// _hi
// his
// is_
// e_t
// en_
// e_o
// t_t
// tio
// _Th
// age
// agePerReview
// reviewsPerUserStdDev
// discussionCount
// reviewCount
// registeredReviewCount
// anonymouseReviewCount
// registeredAnonymouseReviewRatio
// userCount
// occasionalUserCount
// registeredUserCount
// anonymouseUserCount
// registerdAnonymouseUserRatio
// mostActiveUsersReviewCount
