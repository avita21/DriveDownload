# DriveDownload
Download image files slowly

# How to Use:
- Download `fix_google_drive.exe`: https://github.com/avita21/DriveDownload/releases/download/v1/fix_google_drive.exe
- Create a new folder
- Move `fix_google_drive.exe` into the new folder
- Copy any Tabletop Simulator save file (`\Tabletop Simulator\Saves\XXX.json`) into the new folder
- Run `fix_google_drive.exe`

![186489852-9fd019fa-bb03-4d07-ab3f-13df0495e67a](https://user-images.githubusercontent.com/22379453/186491214-7a4f4615-1f7a-4686-9cb1-ce8b9016c609.png)

# Once Completed:
- You'll see in the new folder all google drive images used in the save file
- Delete the contents of the Images folder and Images Raw folder in Tabletop Simulator: (`\Tabletop Simulator\Mods\Images` and `\Tabletop Simulator\Mods\ImagesRaw`)
- Copy the image files in the new folder to the Images folder in Tabletop Simulator: (`\Tabletop Simulator\Mods\Images`)
- Run Tabletop Simulator (make sure Mod Caching is on)
- TTS should use the local files!

![186489985-6d90016c-542d-4cc9-8d5d-fade19138d84](https://user-images.githubusercontent.com/22379453/186491239-aad6ca8c-6f46-4d78-b9f6-43a6743bad25.png)

# Troubleshooting:

If you are seeing these errors in the spawned console:
```
Access denied with the following error:

        Cannot retrieve the public link of the file. You may need to change
        the permission to 'Anyone with the link', or have had many accesses.

You may still be able to access the file from the browser
```
This means google drive is limiting your automated downloads for their files:

![186488348-e56ba87d-895f-4c0a-9b64-0f769e987d47](https://user-images.githubusercontent.com/22379453/186491173-8cec8e6a-902b-4244-a93c-f2e05a999fbf.png)


You will need to wait until these messages clear up, and then re-run the program. This may take a couple hours or a day to resolve. (You can also try using a different VPN connection to bypass google.)
