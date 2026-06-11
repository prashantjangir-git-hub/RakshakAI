import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../widgets/section_card.dart';

class WellnessCheckScreen extends StatelessWidget {
  const WellnessCheckScreen({super.key});

  static const routeName = '/wellness';

  @override
  Widget build(BuildContext context) {
    final score = context.watch<AppState>().wellnessRiskScore;

    return Scaffold(
      appBar: AppBar(title: const Text('Daily Wellness Check')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            SectionCard(
              title: 'How are you feeling today?',
              child: Column(
                children: [
                  _QuestionTile(question: 'Are you feeling safe?', onAnswer: (needsHelp) => context.read<AppState>().updateWellness(needsHelp)),
                  const SizedBox(height: 12),
                  _QuestionTile(question: 'Are you feeling healthy?', onAnswer: (needsHelp) => context.read<AppState>().updateWellness(needsHelp)),
                  const SizedBox(height: 12),
                  _QuestionTile(question: 'Do you need assistance?', onAnswer: (needsHelp) => context.read<AppState>().updateWellness(needsHelp)),
                ],
              ),
            ),
            const SizedBox(height: 20),
            SectionCard(
              title: 'Current welfare risk score',
              child: Text('$score / 100', style: Theme.of(context).textTheme.headlineMedium),
            ),
          ],
        ),
      ),
    );
  }
}

class _QuestionTile extends StatelessWidget {
  const _QuestionTile({required this.question, required this.onAnswer});

  final String question;
  final ValueChanged<bool> onAnswer;

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(20)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(question, style: Theme.of(context).textTheme.titleLarge),
          const SizedBox(height: 12),
          Row(
            children: [
              Expanded(child: OutlinedButton(onPressed: () => onAnswer(false), child: const Text('Yes'))),
              const SizedBox(width: 12),
              Expanded(child: FilledButton(onPressed: () => onAnswer(true), child: const Text('Need Help'))),
            ],
          ),
        ],
      ),
    );
  }
}
