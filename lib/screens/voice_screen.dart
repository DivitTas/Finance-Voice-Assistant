import 'package:flutter/material.dart';
import '../widgets/mic_button.dart';
import '../widgets/chat_bubble.dart';
import '../services/api_service.dart';

class VoiceScreen extends StatefulWidget {
  const VoiceScreen({super.key});

  @override
  State<VoiceScreen> createState() => _VoiceScreenState();
}

class _VoiceScreenState extends State<VoiceScreen> {
  final List<Map<String, dynamic>> messages = [];

  void _sendCommand() async {
    setState(() {
      messages.add({"fromUser": true, "text": "🎤 Listening..."});
    });

    final response = await ApiService.sendFakeCommand();

    setState(() {
      messages.add({"fromUser": false, "text": response});
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Voice Assistant"),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView(
              padding: const EdgeInsets.all(20),
              children: messages
                  .map((msg) => ChatBubble(
                        isUser: msg["fromUser"],
                        message: msg["text"],
                      ))
                  .toList(),
            ),
          ),
          MicButton(onPressed: _sendCommand)
        ],
      ),
    );
  }
}