# Vault — Android APK from GitHub Actions

This repository wraps the supplied `cv2.html` Vault app in an Android WebView using Capacitor. The provided PNG is used for the launcher icon.

## Build your APK (no Android Studio needed)

1. Create a new **GitHub repository**.
2. Unzip this package on your computer.
3. Upload **the contents** of the unzipped folder to the repository root (so `.github/workflows/android.yml` is present at the root).
4. Open the repository's **Actions** tab and enable Actions if GitHub asks.
5. Select **Build Android APK**, click **Run workflow**, then **Run workflow** again.
6. Wait for the green check. Open the completed run, scroll to **Artifacts**, and download `vault-debug-apk`.
7. Unzip the artifact and install `app-debug.apk` on your Android device. If prompted, allow installing apps from that source.

You can also push a commit to `main`/`master` and the workflow will run automatically.

## Notes

- The workflow produces a **debug APK** for direct testing/sideloading, not a Play Store release. Play Store distribution requires a signed release build.
- The app is bundled locally in `www/index.html`. Its existing Tailwind CSS and Google Fonts references still load from the internet, so those visual dependencies need connectivity.
- Notes are stored locally in the app's WebView storage. Use the app's built-in JSON export to back them up.
- The app ID is `com.vault.notes`; change it in `capacitor.config.json` before the first build if you want a different package ID.
- This workflow generates the Android project during CI, so you don't need to commit an `android/` folder.
