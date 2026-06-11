import 'package:flutter/material.dart';

import '../models/alert_item.dart';
import '../models/scam_analysis.dart';
import '../models/user_profile.dart';
import '../services/api_service.dart';

class AppState extends ChangeNotifier {
  AppState({ApiService? apiService}) : _apiService = apiService ?? ApiService();

  final ApiService _apiService;

  String? authToken;
  ScamAnalysis? latestAnalysis;
  String latestAnalyzedMessage = '';
  String? sosStatus;
  int wellnessRiskScore = 32;
  final profile = UserProfile(
    name: 'Savitri Devi',
    phone: '9876543210',
    language: 'English',
    medicalConditions: ['Hypertension'],
    medications: ['Amlodipine'],
    emergencyContacts: ['Neha Sharma', 'Ramesh Sharma'],
  );

  final List<AlertItem> recentAlerts = [
    AlertItem(
      title: 'Scam alert saved',
      subtitle: 'A bank impersonation message was flagged as high risk.',
      timeLabel: '3h ago',
    ),
    AlertItem(
      title: 'Wellness reminder',
      subtitle: 'Daily check-in is due by 7:00 PM.',
      timeLabel: 'Now',
    ),
  ];

  Future<void> signInSenior({required String phone, required String otp}) async {
    authToken = await _apiService.login(phone: phone, role: 'senior', otp: otp);
    notifyListeners();
  }

  Future<void> analyzeMessage(String text) async {
    latestAnalyzedMessage = text.trim();
    latestAnalysis = await _apiService.analyzeScam(latestAnalyzedMessage);
    notifyListeners();
  }

  Future<void> sendSos() async {
    sosStatus = await _apiService.triggerSos();
    notifyListeners();
  }

  Future<void> updateWellness(bool needsHelp) async {
    wellnessRiskScore = await _apiService.submitWellnessCheck(needsHelp: needsHelp);
    notifyListeners();
  }

  void saveLatestEvidence() {
    final analysis = latestAnalysis;
    if (analysis == null || latestAnalyzedMessage.isEmpty) {
      throw StateError('Analyze a suspicious message before saving evidence.');
    }

    _prependAlert(
      AlertItem(
        title: 'Evidence saved',
        subtitle: '${analysis.classification} result stored for family review.',
        timeLabel: 'Now',
      ),
    );
    notifyListeners();
  }

  Future<String> reportLatestScam() async {
    final analysis = latestAnalysis;
    if (analysis == null || latestAnalyzedMessage.isEmpty) {
      throw StateError('Analyze a suspicious message before reporting it.');
    }

    final reportId = await _apiService.reportFraud(
      userId: 'usr_senior_1',
      messageText: latestAnalyzedMessage,
      analysis: analysis,
    );

    _prependAlert(
      AlertItem(
        title: 'Fraud report submitted',
        subtitle: 'Police dashboard notified for ${analysis.classification.toLowerCase()} activity.',
        timeLabel: 'Now',
      ),
    );
    notifyListeners();
    return reportId;
  }

  void _prependAlert(AlertItem alert) {
    recentAlerts.insert(0, alert);
    if (recentAlerts.length > 5) {
      recentAlerts.removeLast();
    }
  }
}
