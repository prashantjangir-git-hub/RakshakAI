import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/app_state.dart';
import '../widgets/section_card.dart';
import 'scam_result_screen.dart';

class ScamDetectorScreen extends StatefulWidget {
  const ScamDetectorScreen({super.key});

  static const routeName = '/scam-detector';

  @override
  State<ScamDetectorScreen> createState() => _ScamDetectorScreenState();
}

class _ScamDetectorScreenState extends State<ScamDetectorScreen> {
  final _controller = TextEditingController();
  bool _loading = false;

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  Future<void> _analyze() async {
    setState(() => _loading = true);
    await context.read<AppState>().analyzeMessage(_controller.text);
    if (!mounted) return;
    setState(() => _loading = false);
    Navigator.pushNamed(context, ScamResultScreen.routeName);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Scam Detector')),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Paste or type the suspicious message.', style: Theme.of(context).textTheme.bodyLarge),
            const SizedBox(height: 18),
            TextField(
              controller: _controller,
              maxLines: 7,
              decoration: const InputDecoration(hintText: 'Example: Your bank account is blocked. Click this link now.'),
            ),
            const SizedBox(height: 18),
            SectionCard(
              title: 'Other input methods',
              child: Column(
                children: [
                  ListTile(
                    contentPadding: EdgeInsets.zero,
                    leading: const Icon(Icons.image_outlined),
                    title: const Text('Upload screenshot'),
                    subtitle: const Text('Wire to image picker in the next Flutter run.'),
                    trailing: OutlinedButton(onPressed: () {}, child: const Text('Upload')),
                  ),
                  ListTile(
                    contentPadding: EdgeInsets.zero,
                    leading: const Icon(Icons.mic_none_rounded),
                    title: const Text('Record voice message'),
                    subtitle: const Text('Helpful for seniors who prefer speaking.'),
                    trailing: OutlinedButton(onPressed: () {}, child: const Text('Record')),
                  ),
                ],
              ),
            ),
            const SizedBox(height: 20),
            SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _loading ? null : _analyze,
                style: FilledButton.styleFrom(padding: const EdgeInsets.symmetric(vertical: 18)),
                child: Text(_loading ? 'Analyzing...' : 'Check message'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
