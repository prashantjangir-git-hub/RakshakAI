import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../widgets/section_card.dart';

class FamilyAlertsScreen extends StatelessWidget {
  const FamilyAlertsScreen({super.key});

  static const routeName = '/family-alerts';

  @override
  Widget build(BuildContext context) {
    final alerts = context.watch<AppState>().recentAlerts;

    return Scaffold(
      appBar: AppBar(title: const Text('Family Alerts')),
      body: Padding(
        padding: const EdgeInsets.all(24),
        child: SectionCard(
          title: 'Latest notifications',
          child: Column(
            children: alerts
                .map(
                  (alert) => ListTile(
                    contentPadding: EdgeInsets.zero,
                    leading: const Icon(Icons.notifications_active_outlined),
                    title: Text(alert.title),
                    subtitle: Text(alert.subtitle),
                    trailing: Text(alert.timeLabel),
                  ),
                )
                .toList(),
          ),
        ),
      ),
    );
  }
}
