'''
1. hide visible geo
2. run script
3. disable or delete the selected geo
4. unhide visible geo
-- project cleaned --
'''
import unreal, sys 

# Get all assets
all_assets =  actors = unreal.EditorLevelLibrary.get_all_level_actors()
all_static_meshes = []
all_lights = []

for myItem in all_assets:

    if isinstance(myItem, unreal.StaticMeshActor):
        all_static_meshes.append(myItem)

    if isinstance(myItem, unreal.PointLight):
        all_lights.append(myItem)


# Function to select assets in the Content Browser
def select_assets_in_content_browser(assets):
    assets[0].set_actor_hidden_in_game(False)
    unreal.EditorLevelLibrary.set_selected_level_actors(assets)

selectme = all_lights

select_assets_in_content_browser(selectme)
print(f"Selected {len(selectme)} assets in the Content Browser.")


