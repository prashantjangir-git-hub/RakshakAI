import 'package:flutter/material.dart';

class AppTheme {
  static const Color navy = Color(0xFF0B1730);
  static const Color teal = Color(0xFF39B7B0);
  static const Color red = Color(0xFFD84E5B);
  static const Color ivory = Color(0xFFF8F4EE);

  static ThemeData build() {
    final scheme = ColorScheme.fromSeed(
      seedColor: teal,
      brightness: Brightness.light,
      primary: navy,
      secondary: teal,
      surface: ivory,
      error: red,
    );

    return ThemeData(
      useMaterial3: true,
      colorScheme: scheme,
      scaffoldBackgroundColor: ivory,
      textTheme: const TextTheme(
        headlineLarge: TextStyle(fontSize: 30, fontWeight: FontWeight.w700, color: navy),
        headlineMedium: TextStyle(fontSize: 24, fontWeight: FontWeight.w700, color: navy),
        titleLarge: TextStyle(fontSize: 20, fontWeight: FontWeight.w700, color: navy),
        bodyLarge: TextStyle(fontSize: 16, color: navy),
        bodyMedium: TextStyle(fontSize: 14, color: navy),
      ),
      cardTheme: CardThemeData(
        color: Colors.white,
        elevation: 0,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
      ),
      inputDecorationTheme: InputDecorationTheme(
        filled: true,
        fillColor: Colors.white,
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(18),
          borderSide: BorderSide.none,
        ),
      ),
    );
  }
}
