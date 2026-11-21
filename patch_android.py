import os

manifest_path = "android/app/src/main/AndroidManifest.xml"
with open(manifest_path, "r", encoding="utf-8") as f:
    manifest = f.read()

if "screenOrientation" not in manifest:
    manifest = manifest.replace(
        "<activity",
        '<activity\n            android:screenOrientation="portrait"',
        1,
    )
    with open(manifest_path, "w", encoding="utf-8") as f:
        f.write(manifest)

res_vals = "android/app/src/main/res/values"
os.makedirs(res_vals, exist_ok=True)

colors_xml = """<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="colorPrimary">#090D16</color>
    <color name="colorPrimaryDark">#090D16</color>
    <color name="colorAccent">#F59E0B</color>
</resources>
"""
with open(os.path.join(res_vals, "colors.xml"), "w", encoding="utf-8") as f:
    f.write(colors_xml)

styles_path = os.path.join(res_vals, "styles.xml")
if os.path.exists(styles_path):
    with open(styles_path, "r", encoding="utf-8") as f:
        styles = f.read()
    if "android:statusBarColor" not in styles:
        target = '<item name="colorPrimaryDark">@color/colorPrimaryDark</item>'
        replacement = (
            target
            + '\n        <item name="android:statusBarColor">#090D16</item>'
            + '\n        <item name="android:navigationBarColor">#090D16</item>'
            + '\n        <item name="android:windowBackground">#090D16</item>'
        )
        styles = styles.replace(target, replacement)
        with open(styles_path, "w", encoding="utf-8") as f:
            f.write(styles)

print("Android manifest & dark theme patched successfully.")
