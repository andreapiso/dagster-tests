from dagster import MetadataValue, Output, asset, Definitions, SourceAsset, AssetKey, MetadataValue

hackernews_top_stories = SourceAsset(key=AssetKey('hackernews_top_stories'))

@asset(name='describe_hn_dataframe', group_name='describe')
def describe_hn_df(hackernews_top_stories):
    df = hackernews_top_stories.describe()
    metadata = {
        "preview": MetadataValue.md(df.to_markdown())
    }
    return Output(value=df, metadata=metadata)

defs = Definitions(assets=[hackernews_top_stories, describe_hn_df])