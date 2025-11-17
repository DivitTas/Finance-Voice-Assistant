import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'theme/dark_theme.dart';
import 'theme/light_theme.dart';
import 'screens/login_screen.dart';
import 'services/app_state.dart';

void main() {
  runApp(ChangeNotifierProvider(create: (_) => AppState(), child: const VoiceBankingApp()));
}

class VoiceBankingApp extends StatelessWidget {
  const VoiceBankingApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Consumer<AppState>(builder: (context, state, _) {
      return MaterialApp(
        debugShowCheckedModeBanner: false,
        title: 'VoiceBank',
        theme: lightTheme,
        darkTheme: darkTheme,
        themeMode: state.isDark ? ThemeMode.dark : ThemeMode.light,
        home: const LoginScreen(),
      );
    });
  }
}