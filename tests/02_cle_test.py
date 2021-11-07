from config import DefaultConfig

def test_cle_insight():
    
    assert DefaultConfig.APPINSIGHTS_INSTRUMENTATION_KEY == '67c867fa-3776-4fd5-8bb0-b6dafe9c68fc'
    
def test_cle_luis():
    
    assert DefaultConfig.LUIS_API_KEY == '362cb200c2de40fd92cd3c0424bb2391'
    
