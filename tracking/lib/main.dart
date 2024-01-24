import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:provider/provider.dart';
import 'package:tracking/src/Provider/CartProvider.dart';
import 'package:tracking/src/Screens/Profile.dart';
import 'package:tracking/src/Screens/Sample.dart';
import 'package:tracking/src/Screens/History.dart';
import 'package:tracking/src/Screens/Club.dart';
import 'package:tracking/src/Screens/Ticketing.dart';
import 'package:tracking/src/Screens/Notification.dart';
import 'package:tracking/src/Screens/Cart.dart';
import 'package:tracking/src/Screens/Login.dart';
import 'package:tracking/src/Screens/Home.dart';
// function to trigger app build
void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {

  const MyApp({Key? key}) : super(key: key);



  @override
  Widget build(BuildContext context) {
    return ChangeNotifierProvider(
        create: (_) => CartProvider(),
        child: MaterialApp(
      
      localizationsDelegates: const [
        GlobalCupertinoLocalizations.delegate,
        GlobalMaterialLocalizations.delegate,
        GlobalWidgetsLocalizations.delegate,
      ],
      supportedLocales: const [
        Locale("fa", "IR"), // OR Locale('ar', 'AE') OR Other RTL locales
      ],
      locale: const Locale("fa", "IR"), // OR Locale('ar', 'AE') OR Other RTL locales,
      initialRoute: '/login',
      routes: {
        '/login': (context) => const SignIn(),
        // When navigating to the "/" route, build the FirstScreen widget.
        '/': (context) => Home(),
        // When navigating to the "/second" route, build the SecondScreen widget.
        '/profile': (context) => const ProfileScreen(),
        '/club': (context) => const ClubScreen(),
        '/ticketing': (context) => const TicketingScreen(),
        '/samples': (context) => const SampleScreen(),
        '/history': (context) => const HistoryScreen(),
        '/notifications': (context) => const NotificationScreen(),
        '/cart': (context) => const CartScreen(),
      },
      debugShowCheckedModeBanner: false,
    ));
  }
}
