import 'package:flutter/material.dart';
import 'home_screen.dart';
import '../services/app_state.dart';
import 'package:provider/provider.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({super.key});

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController _pinController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(30),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.mic, size: 80, color: Theme.of(context).colorScheme.primary),
            const SizedBox(height: 30),
            Text(
              "VoiceBank Login",
              style: TextStyle(
                fontSize: 28,
                fontWeight: FontWeight.bold,
                color: Theme.of(context).colorScheme.primary,
              ),
            ),

            const SizedBox(height: 40),
            TextField(
              controller: _pinController,
              obscureText: true,
              decoration: const InputDecoration(
                labelText: "Enter PIN",
                border: OutlineInputBorder(),
              ),
            ),

            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                if (_pinController.text == "1234") {
                  Navigator.pushReplacement(
                    context,
                    MaterialPageRoute(builder: (context) => const HomeScreen()),
                  );
                } else {
                  ScaffoldMessenger.of(context).showSnackBar(
                    const SnackBar(content: Text("Incorrect PIN")),
                  );
                }
              },
              child: const Text("Login"),
            ),

            const SizedBox(height: 20),
            TextButton(
              onPressed: () {
                Provider.of<AppState>(context, listen: false).toggleTheme();
              },
              child: const Text("Toggle Dark/Light Mode"),
            )
          ],
        ),
      ),
    );
  }
}