import 'package:flutter/material.dart';

final ThemeData darkTheme = ThemeData(
  brightness: Brightness.dark,
  scaffoldBackgroundColor: Colors.black,
  appBarTheme: const AppBarTheme(
    backgroundColor: Colors.transparent,
    elevation: 0,
    foregroundColor: Colors.white,
  ),
  colorScheme: const ColorScheme.dark(
    primary: Color(0xff00eaff),
    secondary: Color(0xffbc00ff),
  ),
  textTheme: const TextTheme(
    bodyMedium: TextStyle(color: Colors.white70),
  ),
);