import wx
import 
basejson = { 
    "#comment": "ShipWreck - Pandemonium - Snowbird | ELM: Ver-10.2 [RFL v1.23]", "objects": [ { "objclass": "LevelDefinition", "objdata": { "StartingSun": 300, "Description": "{PLAYER}'s Search For Scubert II", "GameOverDialogShowBrain": False, "Loot": "RTID(NoLoot@LevelModules)", "ResourceGroupNames": [ "Tombstone_Dark_Special", "Tombstone_Dark_Effects", "ZombieParrotrousleGroup", "ZombiePirateCaptainGroup", "ZombieCarnieMagicianGroup", "ZombieCarnieDoveGroup", "ZombieWestChickenGroup" ], "Modules": [ "RTID(PirateCannonTutorial@CurrentLevel)", "RTID(CannonMinigame@CurrentLevel)", "RTID(ChallengeModule@CurrentLevel)", "RTID(ZombiesDeadWinCon@LevelModules)", "RTID(NewWaves@CurrentLevel)", "RTID(IPP@CurrentLevel)", "RTID(GI@CurrentLevel)", "RTID(Rails@CurrentLevel)" ], "MusicType": "MiniGame_B", "Name": "ShipWreck - BONUS - SNowbird - TEST", "NormalPresentTable": "pirate_normal_01", "ReplayRewardParam": "none", "ReplayRewardType": "none", "ShinyPresentTable": "pirate_shiny_01", "StageModule": "RTID(PirateStage@LevelModules)", "UseTutorialOutro": False, "SuppressDynamicTutorial": True } }, { "aliases": [ "PirateCannonTutorial" ], "objclass": "PirateCannonTutorialProperties", "objdata": { "ResourceGroupNames": [], "ShowTutorial": True } }, { "aliases": [ "ChallengeModule" ], "objclass": "StarChallengeModuleProperties", "objdata": { "Challenges": [ [ "RTID(BeatTheLevel@CurrentLevel)" ] ], "ChallengesAlwaysAvailable": True } }, { "aliases": [ "BeatTheLevel" ], "objclass": "StarChallengeBeatTheLevelProps", "objdata": { "Description": "[STARCHALLENGE_CANNON_MINIGAME]", "DescriptiveName": "[STARCHALLENGE_CANNON_MINIGAME_NAME]" } }, {"aliases":["GI"], "objclass":"InitialGridItemProperties", "objdata":{ "InitialGridItemPlacements": [ {"GridX": 4, "GridY": 2, "TypeName":"effect_nighttime"}, {"GridX": 4, "GridY": 1, "TypeName":"gravestone_pirate"}, {"GridX": 1, "GridY": 2, "TypeName":"SpawnCoconut@."} ] }}, {"aliases":["IPP"], "objclass": "InitialPlantProperties", "objdata": { "InitialPlantPlacements": [ {"GridX": 2, "GridY": 0, "Level": -1, "TypeName":"coconutcannon", "Condition": "icecubed"}, {"GridX": 2, "GridY": 1, "Level": -1, "TypeName":"coconutcannon", "Condition": "icecubed"}, {"GridX": 2, "GridY": 2, "Level": -1, "TypeName":"coconutcannon", "Condition": "icecubed"}, {"GridX": 2, "GridY": 3, "Level": -1, "TypeName":"coconutcannon", "Condition": "icecubed"}, {"GridX": 2, "GridY": 4, "Level": -1, "TypeName":"coconutcannon", "Condition": "icecubed"}, {"GridX": 0, "GridY": 2, "Level": -1, "TypeName":"magnifyinggrass"} ] }}, {"aliases": ["Rails"], "objclass": "RailcartProperties", "objdata": { "RailcartType": "railcart_pirate", "Railcarts": [ {"Column": 0, "Row": 2} ], "Rails": [ {"Column": 0, "RowEnd": 0, "RowStart": 0}, {"Column": 0, "RowEnd": 1, "RowStart": 1}, {"Column": 0, "RowEnd": 2, "RowStart": 2}, {"Column": 0, "RowEnd": 3, "RowStart": 3}, {"Column": 0, "RowEnd": 4, "RowStart": 4} ] }}, { "aliases": [ "CannonMinigame" ], "objclass": "CannonMinigameProperties", "objdata": { "BaseMovementRate": 80, "BaseZombieKillScore": 100, "BufferDistance": 50, "ComboBrackets": [ { "AudioCue": "Play_CrazyDave_Short", "Exclamations": [ "[DAVE_CANNONMINIGAME_3_KILLED_1]", "[DAVE_CANNONMINIGAME_3_KILLED_2]", "[DAVE_CANNONMINIGAME_3_KILLED_3]" ], "MessageColor": { "mAlpha": 255, "mBlue": 220, "mGreen": 255, "mRed": 220 }, "ScoreMultiplier": 2, "ZombiesKilled": 3 }, { "AudioCue": "Play_CrazyDave_Scream", "Exclamations": [ "[DAVE_CANNONMINIGAME_5_KILLED_1]", "[DAVE_CANNONMINIGAME_5_KILLED_2]", "[DAVE_CANNONMINIGAME_5_KILLED_3]" ], "MessageColor": { "mAlpha": 255, "mBlue": 255, "mGreen": 220, "mRed": 220 }, "ScoreMultiplier": 3, "ZombiesKilled": 5 }, { "AudioCue": "Play_CrazyDave_Scream2", "Exclamations": [ "[DAVE_CANNONMINIGAME_8_KILLED_1]", "[DAVE_CANNONMINIGAME_8_KILLED_2]", "[DAVE_CANNONMINIGAME_8_KILLED_3]" ], "MessageColor": { "mAlpha": 255, "mBlue": 220, "mGreen": 240, "mRed": 255 }, "ScoreMultiplier": 4, "ZombiesKilled": 8 }, { "AudioCue": "Play_CrazyDave_Crazy", "Exclamations": [ "[DAVE_CANNONMINIGAME_12_KILLED_1]", "[DAVE_CANNONMINIGAME_12_KILLED_2]", "[DAVE_CANNONMINIGAME_12_KILLED_3]" ], "MessageColor": { "mAlpha": 255, "mBlue": 200, "mGreen": 200, "mRed": 255 }, "ScoreMultiplier": 5, "ZombiesKilled": 12 }, { "AudioCue": "Play_CrazyDave_Crazy", "Exclamations": [ "ABSOLUTE CINEMA" ], "MessageColor": { "mAlpha": 255, "mBlue": 0, "mGreen": 0, "mRed": 255 }, "ScoreMultiplier": 6, "ZombiesKilled": 15 }                ], "Lanes": [ { "SplinePoints": [ {"x": 802, "y": 220}, {"x": 738, "y": 220}, {"x": 674, "y": 220}, {"x": 674, "y": 296}, {"x": 610, "y": 296}, {"x": 610, "y": 372}, {"x": 610, "y": 448}, {"x": 674, "y": 448}, {"x": 674, "y": 524}, {"x": 738, "y": 524}, {"x": 802, "y": 524} ] }, { "SplinePoints": [ {"x": 802, "y": 296}, {"x": 738, "y": 296}, {"x": 674, "y": 372}, {"x": 738, "y": 448}, {"x": 802, "y": 448}, {"x": 546, "y": 600}, {"x": 546, "y": 524}, {"x": 546, "y": 448}, {"x": 546, "y": 372}, {"x": 546, "y": 296}, {"x": 546, "y": 220}, {"x": 546, "y": 144} ] }, { "SplinePoints": [ {"x": 802, "y": 372}, {"x": 738, "y": 372}, {"x": 674, "y": 372}, {"x": 610, "y": 372}, {"x": 546, "y": 372}, {"x": 610, "y": 372}, {"x": 674, "y": 372}, {"x": 738, "y": 372}, {"x": 802, "y": 372}, {"x": 610, "y": 600}, {"x": 610, "y": 524}, {"x": 610, "y": 448}, {"x": 610, "y": 372}, {"x": 610, "y": 296}, {"x": 610, "y": 220}, {"x": 610, "y": 144} ] }, { "SplinePoints": [ {"x": 802, "y": 448}, {"x": 738, "y": 448}, {"x": 674, "y": 372}, {"x": 738, "y": 296}, {"x": 802, "y": 296}, {"x": 546, "y": 144}, {"x": 546, "y": 220}, {"x": 546, "y": 296}, {"x": 546, "y": 372}, {"x": 546, "y": 448}, {"x": 546, "y": 524}, {"x": 546, "y": 600} ] }, { "SplinePoints": [ {"x": 802, "y": 524}, {"x": 738, "y": 524}, {"x": 674, "y": 524}, {"x": 674, "y": 448}, {"x": 610, "y": 448}, {"x": 610, "y": 372}, {"x": 610, "y": 296}, {"x": 674, "y": 296}, {"x": 674, "y": 220}, {"x": 738, "y": 220}, {"x": 802, "y": 220} ] } ], "MaxRewardGold": 110, "MinRewardGold": 100, "MinScore": 25000, "ResourceGroupNames": [], "RowHasCannon": [ 0, 0, 0, 0, 0 ], "SlowdownMovementRate": 45 } }, { "aliases": [ "NewWaves" ], "objclass": "WaveManagerModuleProperties", "objdata": { "WaveManagerProps": "RTID(WaveManagerProps@CurrentLevel)" } }, { "aliases": [ "WaveManagerProps" ], "objclass": "WaveManagerProperties", "objdata": { "FlagWaveInterval": 7, "SuppressFlagZombie": True, "WaveCount": 14, "WaveSpendingPointIncrement": 60, "WaveSpendingPoints": 600, "Waves": [ [ "RTID(Wave1@CurrentLevel)" ] ] } }, { "aliases": ["Wave1"], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "AddToZombiePool": [ { "Type": "RTID(seagull@ZombieTypes)" } ], "Zombies": [ { "Row": "1", "Type": "RTID(pirate_captain_parrot@ZombieTypes)" }, { "Row": "1", "Type": "RTID(parrotrousle_parrot@ZombieTypes)" }, { "Row": "1", "Type": "RTID(pirate_captain_parrot@ZombieTypes)" } ] } }, { "aliases": [ "Wave2" ], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "Zombies": [ { "Row": "5", "Type": "RTID(pirate_captain_parrot@ZombieTypes)" }, { "Row": "5", "Type": "RTID(parrotrousle_parrot@ZombieTypes)" }, { "Row": "5", "Type": "RTID(pirate_captain_parrot@ZombieTypes)" } ] } }, { "aliases": [ "Wave3" ], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "Zombies": [ { "Row": "4", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "4", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "4", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" } ] } }, { "aliases": [ "Wave4" ], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "Zombies": [ { "Row": "3", "Type": "RTID(pelican@ZombieTypes)" }, { "Row": "3", "Type": "RTID(pelican@ZombieTypes)" }, { "Row": "3", "Type": "RTID(pelican@ZombieTypes)" } ] } }, { "aliases": [ "Wave5" ], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "Zombies": [ { "Row": "1", "Type": "RTID(parrotrousle_parrot@ZombieTypes)" }, { "Row": "1", "Type": "RTID(parrotrousle_parrot@ZombieTypes)" }, { "Row": "5", "Type": "RTID(parrotrousle_parrot@ZombieTypes)" }, { "Row": "5", "Type": "RTID(parrotrousle_parrot@ZombieTypes)" } ] } }, { "aliases": [ "Wave6" ], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "Zombies": [ { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" }, { "Row": "2", "Type": "RTID(seagull@ZombieTypes)" } ] } }, { "aliases": [ "Wave7" ], "objclass": "SpawnZombiesJitteredWaveActionProps", "objdata": { "Zombies": [ { "Row": "5", "Type": "RTID(pelican@ZombieTypes)" }, { "Row": "5", "Type": "RTID(pelican@ZombieTypes)" }, { "Row": "5", "Type": "RTID(pelican@ZombieTypes)" } ] } }, {"aliases":["GridSpawn2"], "objclass": "SpawnGravestonesWaveActionProps", "objdata": { "GravestonePool": [ {"Count": 99, "Type": "RTID(SpawnCoconut@.)"}, {"Count": 99, "Type": "RTID(SpawnCoconut@.)"}, {"Count": 99, "Type": "RTID(SpawnCoconut@.)"}, {"Count": 99, "Type": "RTID(SpawnCoconut@.)"}, {"Count": 99, "Type": "RTID(SpawnCoconut@.)"} ], "SpawnPositionsPool": [{"mX": 3, "mY": 0}, {"mX": 2, "mY": 1}, {"mX": 2, "mY": 3}, {"mX": 3, "mY": 4}], "SpawnEffectAnimID": "POPANIM_EFFECTS_PLANT_BURNT", "SpawnSoundID": "Play_Zomb_Egypt_TombRaiser_Grave_Rise", "DisplacePlants": True, "RandomPlacement": True, "ShakeScreen": True, "GridClassesToDestroy": [] }}, {"aliases":["SpawnCoconut"], "objclass":"GridItemType", "objdata":{ "TypeName":"presentPlantOnDestruction", "GridItemClass":"GridItemGravestonePlantOnDestruction", "ResourceGroups":[ "Xmas_Gravestone" ], "Properties":"RTID(PlantSpawnCoconut@.)" }}, { "aliases":[ "PlantSpawnCoconut" ], "objclass":"GridItemGravestonePlantOnDestructionPropertySheet", "objdata":{ "ArtCenter":{ "x":98, "y":127 }, "BreakEffect":"POPANIM_EFFECTS_TOMBSTONE_XMAS_GRAVESTONE_DAMAGE", "BreakEffectSound":"", "DamageStateCount":5, "HitRectOffsetWidth":-30, "HitRectOffsetX":15, "Hitpoints":1, "PopAnim":"POPANIM_GRAVESTONES_XMAS_GRAVESTONE", "ScaledProps":[ { "Arg1":1.3, "Arg2":0.05, "Formula":"standard", "Key":"Hitpoints" } ], "PlantTypeToSpawn":"coconutcannon" } } ], "version": 1 }
count = 1
zombies = ["pirate_captain_parrot","parrotrousle_parrot",'seagull','pelican','skycity_battleplane']
class GridApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Interactive Button Grid", size=(150*len(zombies), 600))
        
        # Main panel
        self.panel = wx.Panel(self)
        
        # List to store dictionaries
        self.data_list = []
        
        # Create the grid of buttons
        self.create_grid()
        
        # Create status bar
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetStatusText("Ready")
        
        # Center the window
        self.Centre()
        
    def create_grid(self):
        # Create a grid sizer (5 rows, 6 columns)
        grid_sizer = wx.GridSizer(rows=6, cols=len(zombies), vgap=5, hgap=5)
        
        # Add buttons 1-25 followed by the 5 special function buttons
        for row in range(6):  # 6 rows
            for col, entity_type in enumerate(zombies):  # depending on how many zombies
                # Calculate the position in the grid (0-29)
                position = row * 6 + col
                
                if position < 6*len(zombies):
                    # Numbered buttons (1-25)
                    btn = wx.Button(self.panel, label=f"{entity_type}{row}")
                    btn.Bind(wx.EVT_BUTTON, self.on_numbered_button)
                    grid_sizer.Add(btn, 1, wx.EXPAND)
                else:
                    # Special function buttons
                    func_position = position - 6*len(zombies)  # 0-4
                    
                    if func_position == 0:
                        # Button 1: Clear list after confirmation
                        clear_btn = wx.Button(self.panel, label="Clear List")
                        clear_btn.Bind(wx.EVT_BUTTON, self.on_clear_list)
                        grid_sizer.Add(clear_btn, 1, wx.EXPAND)
                    elif func_position == 1:
                        # Button 2: Delete last item
                        delete_btn = wx.Button(self.panel, label="Delete Last")
                        delete_btn.Bind(wx.EVT_BUTTON, self.on_delete_last)
                        grid_sizer.Add(delete_btn, 1, wx.EXPAND)
                    elif func_position == 2:
                        # Button 3: Show list
                        show_btn = wx.Button(self.panel, label="Show List")
                        show_btn.Bind(wx.EVT_BUTTON, self.on_show_list)
                        grid_sizer.Add(show_btn, 1, wx.EXPAND)
                    elif func_position == 3:
                        # Button 4: NextWave
                        NextWave_btn = wx.Button(self.panel, label="NextWave")
                        NextWave_btn.Bind(wx.EVT_BUTTON, self.on_nextwave)
                        grid_sizer.Add(NextWave_btn, 1, wx.EXPAND)
                    elif func_position == 4:
                        # Button 5: Exit
                        exit_btn = wx.Button(self.panel, label="Exit")
                        exit_btn.Bind(wx.EVT_BUTTON, self.on_exit)
                        grid_sizer.Add(exit_btn, 1, wx.EXPAND)
        
        # Set the sizer for the panel
        self.panel.SetSizer(grid_sizer)
    
    def on_numbered_button(self, event):
        # Get the button entity_type
        btn = event.GetEventObject()
        entity_type = btn.GetLabel()
        
        # Create a dictionary and append to the list
        data = {"Row": int(entity_type[-1]), "Type": f"RTID({entity_type[:-1]}@ZombieTypes)"}
        self.data_list.append(data)
        
        # Update the status bar
        self.status_bar.SetStatusText(f"Added: {data}")
    
    def on_clear_list(self, event):
        # Show confirmation dialog
        dlg = wx.MessageDialog(
            self, 
            "Are you sure you want to clear the list?",
            "Confirmation",
            wx.YES_NO | wx.ICON_QUESTION
        )
        
        result = dlg.ShowModal()
        if result == wx.ID_YES:
            # Clear the list
            self.data_list.clear()
            self.status_bar.SetStatusText("List cleared")
        
        dlg.Destroy()
    
    def on_delete_last(self, event):
        if self.data_list:
            # Remove the last item
            removed = self.data_list.pop()
            self.status_bar.SetStatusText(f"Removed: {removed}")
        else:
            self.status_bar.SetStatusText("List is empty")
    
    def on_show_list(self, event):
        # Create a new frame to display the list
        list_frame = ListFrame(self, self.data_list)
        list_frame.Show()
    
    def on_nextwave(self, event):
        # Show a NextWave message
        global count
        count += 1
        basejson['objects'][9]['objdata']['Waves'].append([f"RTID(Wave{count}@CurrentLevel)"])
        basejson['objects'].append(self.data_list)
        dlg.ShowModal()
        dlg.Destroy()
    
    def on_exit(self, event):
        # Close the application
        self.Close()


class ListFrame(wx.Frame):
    def __init__(self, parent, data_list):
        super().__init__(parent, title="List Contents", size=(400, 300))
        
        panel = wx.Panel(self)
        
        # Create a text control to display the list
        self.text_ctrl = wx.TextCtrl(
            panel,
            style=wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
        )
        
        # Format and display the list contents
        content = ""
        for i, item in enumerate(data_list):
            content += f"Item {i+1}: {item}\n"
        
        if not content:
            content = "List is empty"
            
        self.text_ctrl.SetValue(content)
        
        # Create a sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text_ctrl, 1, wx.ALL | wx.EXPAND, 10)
        
        # Add a close button
        close_btn = wx.Button(panel, label="Close")
        close_btn.Bind(wx.EVT_BUTTON, self.on_close)
        sizer.Add(close_btn, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(sizer)
        
        # Center the window relative to the parent
        self.Centre()
    
    def on_close(self, event):
        self.Close()


if __name__ == "__main__":
    app = wx.App()
    frame = GridApp()
    frame.Show()
    app.MainLoop()
