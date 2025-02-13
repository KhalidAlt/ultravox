from ultravox.data import types

YT_BASE_CONFIG = types.DatasetConfig(
    name="yt_v0",
    path="SynthiaLab/yt_v0",
    transcript_template="{{sentence}}",
    assistant_template="{{sentence}}",
)

YT_AR_CONFIG = types.DatasetConfig(
    name="yt_v0-ar",
    base="yt_v0",
    subset="ar",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=5003),
        types.DatasetSplitConfig(name="validation", num_samples=264),

    ],
)


YT_AR_TRANS_CONFIG = types.DatasetConfig(
    name="yt_v0-ar-transcription",
    base="yt_v0-ar",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)

YT_AR_CONT_CONFIG = types.DatasetConfig(
    name="yt_v0-ar-continuation",
    base="yt_v0-ar",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)

configs = [
    YT_BASE_CONFIG,
    YT_AR_CONFIG,
    YT_AR_TRANS_CONFIG,
    YT_AR_CONT_CONFIG,
]

