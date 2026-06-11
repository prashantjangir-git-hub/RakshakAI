class UserProfile {
  final String name;
  final String phone;
  final String language;
  final List<String> medicalConditions;
  final List<String> medications;
  final List<String> emergencyContacts;

  UserProfile({
    required this.name,
    required this.phone,
    required this.language,
    required this.medicalConditions,
    required this.medications,
    required this.emergencyContacts,
  });
}
