# Dead Cells Archipelago Setup Guide

## Required Software

- Dead Cells from: [Steam](https://store.steampowered.com/app/588650/Dead_Cells/)
- Dead Cells Archipelago Client from: [Dead Cells AP Releases Page](https://github.com/DenFlyvendeGris/DeadCells_Archipelago/releases/)

## Optional Software

- Dead Cells AP Tracker
    - PopTracker from: [PopTracker Releases Page](https://github.com/black-sliver/PopTracker/releases/)

## Installation Procedures (Windows)

1. Download the Dead Cells Archipelago Client release and extract it to a folder of your choice.

2. Make sure Dead Cells is installed via Steam.

3. Place the extracted mod files into your Dead Cells mods folder, typically located at:
   `C:\Users\<YourName>\AppData\Roaming\Motion Twin\Dead Cells\mods\`

## Joining a MultiWorld Game

1. Before launching the game, edit the `AP.json` file in the Dead Cells AP Client folder.

2. For the `Url` field, enter the address of the Archipelago server, such as `archipelago.gg:38281`.
   Your server host should be able to tell you this.

3. For the `SlotName` field, enter your "name" field from your YAML or website config.

4. For the `Password` field, enter the server password if one exists; otherwise leave this field blank.

5. Save the file and launch Dead Cells through Steam. If the Archipelago connection indicator
   appears in the top left of the screen, you are successfully connected.

An example `AP.json` file:

```json
{
    "Url": "archipelago.gg:12345",
    "SlotName": "BeheadedPlayer",
    "Password": ""
}
```

## Important Notes

- Elite enemy kill checks are **permanent across runs**. Each elite type only needs to be killed
  once across your entire playthrough, not once per run.

- Received items (blueprints, runes, scrolls) are added to your permanent unlock pool and will
  be available at the start of each new run once received.

- If you disconnect mid-run, the client will automatically attempt to reconnect. Any checks
  collected while offline will be sent once the connection is restored.

## Troubleshooting

**The connection indicator does not appear:**
- Double check the `Url`, `SlotName`, and `Password` fields in `AP.json`.
- Make sure the Archipelago server is running and reachable.
- Verify the mod files are placed in the correct Dead Cells mods folder.

**Items are not being received:**
- Make sure you are connected to the server before starting a run.
- Check that your YAML DLC settings match the DLC you have installed.