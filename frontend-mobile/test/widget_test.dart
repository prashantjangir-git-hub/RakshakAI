import 'package:flutter_test/flutter_test.dart';

import 'package:rakshakai_mobile/main.dart';

void main() {
  testWidgets('renders app title on splash', (tester) async {
    await tester.pumpWidget(const RakshakAiApp());

    expect(find.text('RakshakAI'), findsOneWidget);
    await tester.pump(const Duration(seconds: 3));
    await tester.pumpAndSettle();
    expect(find.text('Welcome back'), findsOneWidget);
  });
}
