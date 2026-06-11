import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../theme/app_theme.dart';
import '../widgets/action_button_card.dart';
import '../widgets/section_card.dart';
import 'family_alerts_screen.dart';
import 'profile_screen.dart';
import 'scam_detector_screen.dart';
import 'sos_screen.dart';
import 'wellness_check_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  static const routeName = '/home';

  @override
  Widget build(BuildContext context) {
    final appState = context.watch<AppState>();

    return Scaffold(
      appBar: AppBar(
        title: const Text('RakshakAI'),
        actions: [
          IconButton(onPressed: () => Navigator.pushNamed(context, FamilyAlertsScreen.routeName), icon: const Icon(Icons.notifications_outlined)),
          IconButton(onPressed: () => Navigator.pushNamed(context, ProfileScreen.routeName), icon: const Icon(Icons.person_outline)),
        ],
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(20),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Stay safe today', style: Theme.of(context).textTheme.headlineMedium),
            const SizedBox(height: 6),
            Text('Quick access to emergency, scam checking, and daily wellbeing.', style: Theme.of(context).textTheme.bodyLarge),
            const SizedBox(height: 18),
            ActionButtonCard(
              title: 'SOS',
              subtitle: 'One tap emergency help',
              icon: Icons.sos_rounded,
              color: AppTheme.red,
              onTap: () => Navigator.pushNamed(context, SosScreen.routeName),
            ),
            const SizedBox(height: 16),
            ActionButtonCard(
              title: 'Check Scam',
              subtitle: 'Verify suspicious text or screenshots',
              icon: Icons.security_rounded,
              color: AppTheme.navy,
              onTap: () => Navigator.pushNamed(context, ScamDetectorScreen.routeName),
            ),
            const SizedBox(height: 16),
            ActionButtonCard(
              title: 'Daily Check-In',
              subtitle: 'Share your safety and health status',
              icon: Icons.favorite_outline,
              color: AppTheme.teal,
              onTap: () => Navigator.pushNamed(context, WellnessCheckScreen.routeName),
            ),
            const SizedBox(height: 20),
            SectionCard(
              title: 'Recent alerts',
              child: Column(
                children: appState.recentAlerts
                    .map(
                      (alert) => ListTile(
                        contentPadding: EdgeInsets.zero,
                        title: Text(alert.title),
                        subtitle: Text(alert.subtitle),
                        trailing: Text(alert.timeLabel),
                      ),
                    )
                    .toList(),
              ),
            ),
            const SizedBox(height: 16),
            SectionCard(
              title: 'Safety tip',
              child: Text(
                'Never share OTP, bank PIN, or remote access codes with anyone, even if they say they are from your bank or the police.',
                style: Theme.of(context).textTheme.bodyLarge,
              ),
            ),
          ],
        ),
      ),
    );
  }
}
