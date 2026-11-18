# Petite Power – Android app

The full workout app (weekly plan, 60 animated exercises, timer, progress) packaged as an Android app.
It runs offline, keeps the screen on during workouts and saves your progress on the phone.

## Option A – Build on your PC with Android Studio

1. Install **Android Studio** (free): https://developer.android.com/studio
2. Open Android Studio → **Open** → select this `PetitePowerAndroid` folder.
3. Wait for "Gradle sync" to finish (the first time it downloads Gradle and the Android SDK, about 5–10 minutes).
4. Menu **Build → Build App Bundle(s) / APK(s) → Build APK(s)**.
5. Click **locate** in the pop-up. The file is `app/build/outputs/apk/debug/app-debug.apk`.

## Option B – Let GitHub build it (nothing to install)

1. Create a free GitHub account and a new **private** repository.
2. Upload everything in this folder (including the hidden `.github` folder).
3. Open the **Actions** tab → **Build APK** → wait about 3 minutes for the green tick.
4. Open the run and download **PetitePower-apk** (a zip containing the APK).

## Install on your phone

**Direct download (open on your phone):**
https://github.com/lavanyapro/Female-Exercise/releases/latest/download/PetitePower.apk

1. Open the link above on your phone, or copy the `.apk` to it (USB cable, Google Drive, or email).
2. Tap the file. Android asks to allow installs from that app (Files / Drive / Gmail). Allow it.
3. Tap **Install**, then open **Petite Power** from your home screen.

Play Protect may warn that the app is from an unknown developer. That's normal for apps you build
yourself; choose **Install anyway**.

## Updating the app content

The app page lives in `app/src/main/assets/index.html`. After changing `petite-power.html`, run:

    python tools/bundle_html.py ../petite-power.html

then build the APK again. To update the app on your phone, install the new APK over the old one.
Your saved progress is kept.
