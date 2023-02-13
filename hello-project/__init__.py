from dagster import Definitions

from . import hello_dagster

defs = Definitions(
    assets=[hello_dagster.hackernews_top_story_ids, hello_dagster.hackernews_top_stories]
)

# print(defs.load_asset_value(asset_key='hackernews_top_stories'))