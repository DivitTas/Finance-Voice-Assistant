import 'package:flutter/material.dart';

class MicButton extends StatelessWidget {
  final VoidCallback onPressed;

  const MicButton({super.key, required this.onPressed});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(18),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Theme.of(context).colorScheme.primary,
          shape: const CircleBorder(),
          padding: const EdgeInsets.all(22),
        ),
        onPressed: onPressed,
        child: const Icon(Icons.mic, size: 35, color: Colors.white),
      ),
    );
  }
}