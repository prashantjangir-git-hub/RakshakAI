class ScamAnalysis {
  final int riskScore;
  final String classification;
  final String explanation;
  final String recommendedAction;

  ScamAnalysis({
    required this.riskScore,
    required this.classification,
    required this.explanation,
    required this.recommendedAction,
  });

  factory ScamAnalysis.fromJson(Map<String, dynamic> json) {
    return ScamAnalysis(
      riskScore: json['riskScore'] ?? 0,
      classification: json['classification'] ?? 'SAFE',
      explanation: json['aiExplanation'] ?? 'No explanation available.',
      recommendedAction: json['recommendedAction'] ?? 'Stay alert and verify the sender.',
    );
  }
}
