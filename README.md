# DriveDownload
Download image files slowly

# How to Use:
- Download `fix_google_drive.exe`: https://github.com/avita21/DriveDownload/releases/download/v1/fix_google_drive.exe
- Create a new folder
- Move `fix_google_drive.exe` into the new folder
- Copy any Tabletop Simulator save file (`\Tabletop Simulator\Saves\XXX.json`) into the new folder
- Run `fix_google_drive.exe`

# Once Completed:
- You'll see in the new folder all google drive images used in the save file
- Delete the contents of the Images folder and Images Raw folder in Tabletop Simulator: (`\Tabletop Simulator\Mods\Images` and `\Tabletop Simulator\Mods\ImagesRaw`)
- Copy the image files in the new folder to the Images folder in Tabletop Simulator: (`\Tabletop Simulator\Mods\Images`)
- Run Tabletop Simulator (make sure Mod Caching is on)
- TTS should use the local files!

# Troubleshooting:

If you are seeing these errors in the spawned console:
```
Access denied with the following error:

        Cannot retrieve the public link of the file. You may need to change
        the permission to 'Anyone with the link', or have had many accesses.

You may still be able to access the file from the browser
```
This means google drive is limiting your automated downloads for their files: image

You will need to wait until these messages clear up, and then re-run the program. This may take a couple hours or a day to resolve. (You can also try using a different VPN connection to bypass google.)