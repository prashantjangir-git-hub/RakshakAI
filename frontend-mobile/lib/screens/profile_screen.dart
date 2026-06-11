import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../widgets/section_card.dart';

class ProfileScreen extends StatelessWidget {
  const ProfileScreen({super.key});

  static const routeName = '/profile';

  @override
  Widget build(BuildContext context) {
    final profile = context.watch<AppState>().profile;

    return Scaffold(
      appBar: AppBar(title: const Text('Profile')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          children: [
            SectionCard(
              title: profile.name,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('Phone: ${profile.phone}'),
                  const SizedBox(height: 8),
                  Text('Preferred language: ${profile.language}'),
                ],
              ),
            ),
            const SizedBox(height: 16),
            SectionCard(
              title: 'Medical conditions',
              child: Wrap(spacing: 10, runSpacing: 10, children: profile.medicalConditions.map((item) => Chip(label: Text(item))).toList()),
            ),
            const SizedBox(height: 16),
            SectionCard(
              title: 'Emergency contacts',
              child: Wrap(spacing: 10, runSpacing: 10, children: profile.emergencyContacts.map((item) => Chip(label: Text(item))).toList()),
            ),
          ],
        ),
      ),
    );
  }
}
