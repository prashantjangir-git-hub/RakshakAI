import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'providers/app_state.dart';
import 'screens/family_alerts_screen.dart';
import 'screens/home_screen.dart';
import 'screens/login_screen.dart';
import 'screens/profile_screen.dart';
import 'screens/scam_detector_screen.dart';
import 'screens/scam_result_screen.dart';
import 'screens/sos_screen.dart';
import 'screens/splash_screen.dart';
import 'screens/wellness_check_screen.dart';
import 'theme/app_theme.dart';

void main() {
  runApp(const RakshakAiApp());
}

class RakshakAiApp extends StatelessWidget {
  const RakshakAiApp({super.key});

  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
      create: (_) => AppState(),
      child: MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'RakshakAI',
        theme: AppTheme.build(),
        initialRoute: SplashScreen.routeName,
        routes: {
          SplashScreen.routeName: (_) => const SplashScreen(),
          LoginScreen.routeName: (_) => const LoginScreen(),
          HomeScreen.routeName: (_) => const HomeScreen(),
          SosScreen.routeName: (_) => const SosScreen(),
          ScamDetectorScreen.routeName: (_) => const ScamDetectorScreen(),
          ScamResultScreen.routeName: (_) => const ScamResultScreen(),
          WellnessCheckScreen.routeName: (_) => const WellnessCheckScreen(),
          ProfileScreen.routeName: (_) => const ProfileScreen(),
          FamilyAlertsScreen.routeName: (_) => const FamilyAlertsScreen(),
        },
      ),
    );
  }
}
