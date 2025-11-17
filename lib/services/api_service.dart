import 'dart:async';

class ApiService {
  // 🔥 This is a temporary fake API call
  // Later we replace this with your team's real backend endpoint.
  static Future<String> sendFakeCommand() async {
    await Future.delayed(const Duration(seconds: 1));
    return "Your backend is not connected yet — this is a demo response 👍";
  }

  // Example structure for future real backend call:
  /*
  static Future<String> sendVoiceCommand(Uint8List audio) async {
    final response = await http.post(
      Uri.parse('http://YOUR_BACKEND/transcribe'),
      body: audio,
    );
    return response.body;
  }
  */
}