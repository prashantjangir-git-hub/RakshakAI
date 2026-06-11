import 'package:flutter/material.dart';

class RiskMeter extends StatelessWidget {
  const RiskMeter({super.key, required this.score, required this.label});

  final int score;
  final String label;

  @override
  Widget build(BuildContext context) {
    final color = score >= 75 ? const Color(0xFFD84E5B) : score >= 40 ? const Color(0xFFE0A43B) : const Color(0xFF2E9F7E);

    return Column(
      children: [
        Stack(
          alignment: Alignment.center,
          children: [
            SizedBox(
              height: 120,
              width: 120,
              child: CircularProgressIndicator(
                value: score / 100,
                strokeWidth: 10,
                backgroundColor: color.withValues(alpha: 0.18),
                valueColor: AlwaysStoppedAnimation<Color>(color),
              ),
            ),
            Column(
              children: [
                Text('$score', style: Theme.of(context).textTheme.headlineMedium),
                Text('Risk score', style: Theme.of(context).textTheme.bodyMedium),
              ],
            ),
          ],
        ),
        const SizedBox(height: 12),
        Text(label, style: Theme.of(context).textTheme.titleLarge?.copyWith(color: color)),
      ],
    );
  }
}
