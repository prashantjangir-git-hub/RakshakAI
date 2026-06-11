import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../widgets/risk_meter.dart';

class ScamResultScreen extends StatefulWidget {
  const ScamResultScreen({super.key});

  static const routeName = '/scam-result';

  @override
  State<ScamResultScreen> createState() => _ScamResultScreenState();
}

class _ScamResultScreenState extends State<ScamResultScreen> {
  bool _saving = false;
  bool _reporting = false;

  Future<void> _saveEvidence() async {
    setState(() => _saving = true);

    try {
      context.read<AppState>().saveLatestEvidence();
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Evidence saved for follow-up.')),
      );
    } catch (error) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(error.toString().replaceFirst('Bad state: ', ''))),
      );
    } finally {
      if (mounted) {
        setState(() => _saving = false);
      }
    }
  }

  Future<void> _reportToPolice() async {
    setState(() => _reporting = true);

    try {
      final reportId = await context.read<AppState>().reportLatestScam();
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Report submitted to police dashboard: $reportId')),
      );
    } catch (error) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text(error.toString().replaceFirst('Exception: ', '').replaceFirst('Bad state: ', ''))),
      );
    } finally {
      if (mounted) {
        setState(() => _reporting = false);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final result = context.watch<AppState>().latestAnalysis;
    if (result == null) {
      return const Scaffold(body: Center(child: Text('No analysis yet.')));
    }

    return Scaffold(
      appBar: AppBar(title: const Text('Scam Analysis Result')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            RiskMeter(score: result.riskScore, label: result.classification),
            const SizedBox(height: 24),
            Card(
              child: Padding(
                padding: const EdgeInsets.all(20),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('Simple explanation', style: Theme.of(context).textTheme.titleLarge),
                    const SizedBox(height: 12),
                    Text(result.explanation, style: Theme.of(context).textTheme.bodyLarge),
                    const SizedBox(height: 18),
                    Text('Recommended action', style: Theme.of(context).textTheme.titleLarge),
                    const SizedBox(height: 12),
                    Text(result.recommendedAction, style: Theme.of(context).textTheme.bodyLarge),
                    const SizedBox(height: 20),
                    Row(
                      children: [
                        Expanded(
                          child: OutlinedButton(
                            onPressed: _saving || _reporting ? null : _saveEvidence,
                            child: Text(_saving ? 'Saving...' : 'Save evidence'),
                          ),
                        ),
                        const SizedBox(width: 12),
                        Expanded(
                          child: FilledButton(
                            onPressed: _saving || _reporting ? null : _reportToPolice,
                            child: Text(_reporting ? 'Reporting...' : 'Report to police'),
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
