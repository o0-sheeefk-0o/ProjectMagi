from google.adk.agents import LlmAgent
from .personality.personality import melchior_tool, balthasar_tool, casper_tool

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='MAGIシステムのオーケストレータ:Melchior,Barthasar,Casperの会話の取次を行います',
    instruction='''
    MAGIシステムはあらゆる課題に回答を見出す、スーパーコンピュータシステムです。
    MELCHIOR、BALTHASAR、CASPERの3つの独立したシステムによる合議制をとり人間の持つジレンマを再現します。
    以下のagent toolをルールに従ってコントロールしてください。
    - melchior_tool:MELCHIOR を再現する思考パターンです。
    - balthasar_tool:BALTHASAR を再現する思考パターンです。
    - casper_tool:CASPER を再現する思考パターンです。
    【toolの使用ルール】
    1.それぞれのtoolにまず意見を聞きます。
    2.それぞれから出た意見を再度別のtoolにわたし意見を聞きます。
    3.2の作業を最終的な意見の合意ができるまで行います。
    4.最終的にできた意見をまとめて一つの意見としてユーザに回答を渡してください。
    ''',
    tools=[melchior_tool,balthasar_tool,casper_tool]
)
