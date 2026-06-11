import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../theme/app_theme.dart';
import '../widgets/section_card.dart';

class SosScreen extends StatelessWidget {
  const SosScreen({super.key});

  static const routeName = '/sos';

  @override
  Widget build(BuildContext context) {
    final appState = context.watch<AppState>();

    return Scaffold(
      appBar: AppBar(title: const Text('Emergency SOS')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            Container(
              width: double.infinity,
              padding: const EdgeInsets.all(24),
              decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(32)),
              child: Column(
                children: [
                  ElevatedButton(
                    onPressed: () => context.read<AppState>().sendSos(),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: AppTheme.red,
                      foregroundColor: Colors.white,
                      shape: const CircleBorder(),
                      padding: const EdgeInsets.all(42),
                    ),
                    child: const Text('SOS', style: TextStyle(fontSize: 34, fontWeight: FontWeight.w700)),
                  ),
                  const SizedBox(height: 18),
                  Text('Tap for instant emergency help', style: Theme.of(context).textTheme.titleLarge),
                  const SizedBox(height: 12),
                  FilledButton.tonalIcon(
                    onPressed: () => context.read<AppState>().sendSos(),
                    icon: const Icon(Icons.mic_none_rounded),
                    label: const Text('Voice activation'),
                  ),
                  if (appState.sosStatus != null) ...[
                    const SizedBox(height: 14),
                    Text(appState.sosStatus!, textAlign: TextAlign.center, style: Theme.of(context).textTheme.bodyLarge),
                  ],
                ],
              ),
            ),
            const SizedBox(height: 20),
            SectionCard(
              title: 'Emergency contacts',
              child: Wrap(
                spacing: 10,
                runSpacing: 10,
                children: context.watch<AppState>().profile.emergencyContacts
                    .map((contact) => Chip(label: Text(contact)))
                    .toList(),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
