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



let a = [0.34392857142857142, 0.32749999999999996, 0.34321428571428569, 0.37035714285714283, 0.37857142857142867, 0.38678571428571434, 0.39428571428571441, 0.39428571428571441, 0.40285714285714291, 0.40535714285714286, 0.40000000000000002, 0.40928571428571425, 0.40607142857142858, 0.40107142857142852, 0.4003571428571428, 0.40428571428571425, 0.40285714285714291, 0.40821428571428575, 0.4071428571428572, 0.40392857142857153, 0.40857142857142864, 0.40821428571428575, 0.40357142857142864, 0.40642857142857147, 0.40499999999999997, 0.4071428571428572, 0.40642857142857147, 0.41357142857142859, 0.41678571428571437, 0.41178571428571437, 0.41785714285714287, 0.42000000000000004, 0.4146428571428572, 0.41857142857142859, 0.42107142857142865, 0.4196428571428571, 0.41964285714285721, 0.42071428571428571, 0.41678571428571426, 0.42035714285714282, 0.42142857142857143, 0.4196428571428571, 0.41928571428571432, 0.42035714285714282, 0.42071428571428565, 0.41821428571428576, 0.42000000000000004, 0.42178571428571432, 0.42392857142857149, 0.42035714285714282, 0.42035714285714282, 0.42142857142857137, 0.42107142857142865, 0.41821428571428576, 0.42107142857142854, 0.41714285714285715, 0.41821428571428576, 0.42035714285714282, 0.42142857142857143, 0.42000000000000004, 0.41678571428571426, 0.41750000000000009, 0.41500000000000004, 0.41428571428571431, 0.41750000000000009, 0.41749999999999998, 0.41750000000000009, 0.41857142857142859, 0.41821428571428571, 0.42107142857142865, 0.42035714285714282, 0.42071428571428571, 0.42142857142857143, 0.42178571428571432, 0.42000000000000004, 0.42392857142857138, 0.42214285714285715, 0.42071428571428571, 0.4196428571428571, 0.41928571428571432, 0.42035714285714282, 0.42107142857142854, 0.42071428571428582, 0.42071428571428571, 0.42071428571428571, 0.41857142857142859, 0.41821428571428576, 0.41928571428571432, 0.41642857142857148, 0.41714285714285715, 0.42071428571428571, 0.41750000000000009, 0.41964285714285721, 0.41892857142857148, 0.41928571428571432, 0.42142857142857143, 0.41821428571428571, 0.42000000000000004, 0.41821428571428571]

let max = 0

a.forEach((n) => {
  if (n > max) {
    max = n
  }
})

console.log(a.indexOf(max) + 1);
console.log(a[a.indexOf(max)]);




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
