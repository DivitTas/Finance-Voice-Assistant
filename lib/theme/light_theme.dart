import 'package:flutter/material.dart';

final ThemeData lightTheme = ThemeData(
  brightness: Brightness.light,
  scaffoldBackgroundColor: Colors.white,
  appBarTheme: const AppBarTheme(
    backgroundColor: Colors.transparent,
    elevation: 0,
    foregroundColor: Colors.black,
  ),
  colorScheme: ColorScheme.light(
    primary: Colors.purpleAccent,
    secondary: Colors.cyanAccent,
  ),
  textTheme: const TextTheme(
    bodyMedium: TextStyle(color: Colors.black87),
  ),
);