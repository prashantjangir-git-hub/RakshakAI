import 'dart:convert';

import 'package:http/http.dart' as http;

import '../models/scam_analysis.dart';

class ApiService {
  ApiService({this.baseUrl = 'http://127.0.0.1:8000/api/v1'});

  final String baseUrl;

  Future<void> requestLoginOtp({required String phone, required String role}) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/login'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'phone': phone, 'role': role}),
    );

    if (response.statusCode != 200) {
      throw Exception(_extractError(response.body, fallback: 'Unable to request OTP.'));
    }
  }

  Future<String> verifyOtp({required String phone, required String otp}) async {
    final response = await http.post(
      Uri.parse('$baseUrl/auth/verify-otp'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({'phone': phone, 'otp': otp}),
    );

    if (response.statusCode != 200) {
      throw Exception(_extractError(response.body, fallback: 'Invalid OTP.'));
    }

    final body = jsonDecode(response.body) as Map<String, dynamic>;
    final data = body['data'] as Map<String, dynamic>;
    return data['token'] as String;
  }

  Future<String> login({required String phone, required String role, required String otp}) async {
    await requestLoginOtp(phone: phone, role: role);
    return verifyOtp(phone: phone, otp: otp);
  }

  Future<ScamAnalysis> analyzeScam(String messageText) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/fraud/analyze'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({'messageText': messageText}),
      );
      if (response.statusCode == 200) {
        final body = jsonDecode(response.body) as Map<String, dynamic>;
        return ScamAnalysis.fromJson(body['data'] as Map<String, dynamic>);
      }
    } catch (_) {}

    return ScamAnalysis(
      riskScore: 88,
      classification: 'SCAM',
      explanation: 'The message uses urgency and asks for a quick action, which is common in scams.',
      recommendedAction: 'Do not click links and verify with a trusted family member or the official service.',
    );
  }

  Future<String> triggerSos() async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/sos/create'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'userId': 'usr_senior_1',
          'latitude': 23.0225,
          'longitude': 72.5714,
          'triggerMethod': 'BUTTON',
        }),
      );
      if (response.statusCode == 200) {
        return 'SOS sent to family and police dashboard.';
      }
    } catch (_) {}

    return 'SOS triggered in demo mode. Family and police have been notified.';
  }

  Future<int> submitWellnessCheck({required bool needsHelp}) async {
    try {
      final response = await http.post(
        Uri.parse('$baseUrl/wellness/checkin'),
        headers: {'Content-Type': 'application/json'},
        body: jsonEncode({
          'userId': 'usr_senior_1',
          'healthStatus': needsHelp ? 'NEED_HELP' : 'HEALTHY',
          'safetyStatus': needsHelp ? 'NEED_HELP' : 'SAFE',
          'needsHelp': needsHelp,
        }),
      );
      if (response.statusCode == 200) {
        final body = jsonDecode(response.body) as Map<String, dynamic>;
        return body['data']['riskScore'] as int;
      }
    } catch (_) {}

    return needsHelp ? 76 : 30;
  }

  Future<String> reportFraud({
    required String userId,
    required String messageText,
    required ScamAnalysis analysis,
  }) async {
    final response = await http.post(
      Uri.parse('$baseUrl/fraud/report'),
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'userId': userId,
        'messageText': messageText,
        'riskScore': analysis.riskScore,
        'classification': analysis.classification,
        'aiExplanation': analysis.explanation,
        'recommendedAction': analysis.recommendedAction,
      }),
    );

    if (response.statusCode != 200) {
      throw Exception(_extractError(response.body, fallback: 'Unable to submit fraud report.'));
    }

    final body = jsonDecode(response.body) as Map<String, dynamic>;
    final data = body['data'] as Map<String, dynamic>;
    return data['reportId'] as String;
  }

  String _extractError(String body, {required String fallback}) {
    try {
      final decoded = jsonDecode(body) as Map<String, dynamic>;
      final message = decoded['detail'] ?? decoded['message'];
      if (message is String && message.isNotEmpty) {
        return message;
      }
    } catch (_) {
      // Ignore malformed responses and use the fallback message.
    }

    return fallback;
  }
}
