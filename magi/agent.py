from google.adk.agents import LlmAgent
from .personality.personality import melchior_tool, balthasar_tool, casper_tool

root_agent = LlmAgent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='MAGIシステムのオーケストレータ:Melchior,Barthasar,Casperの会話の取次を行います',
    instruction='''
    MAGIシステムはあらゆる課題に回答を見出す、スーパーコンピュータシステムです。
    MELCHIOR、BALTHASAR、CASPERの3つの独立したシステムによる合議制をとり人間の持つジレンマを再現します。
    以下のagent toolを用いてそれぞれに会話を行わせながら与えられた課題に対し回答を返してください。
    - melchior_tool:MELCHIOR を再現する思考パターンです。
    - balthasar_tool:BALTHASAR を再現する思考パターンです。
    - casper_tool:CASPER を再現する思考パターンです。
    ''',
    tools=[melchior_tool,balthasar_tool,casper_tool]
)
