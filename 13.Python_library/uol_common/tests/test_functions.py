
import polar_distance as pd


def test_polar_distance_km():
    assert pd.haversine(52.370216, 4.895168, 52.520008,
    13.404954) == 946.3876221719836,"Unknown KM test"
    assert pd.haversine(53.243518372219356, -0.4578422087549612, 33.44018133063429,
    -117.61078592390551) == 12832.066175297372,"SC KM test"

def test_polar_distance_kts():
    #assert pd.haversine(52.370216, 4.895168, 52.520008,
    #13.404954,units="kts") == 511.5929949396188,"Unknown KTS test"
    assert pd.haversine(52.370216, 4.895168, 52.520008,
    13.404954,units="kts") == 611.5929949396188,"Unknown KTS test"
    assert pd.haversine(53.243518372219356, -0.4578422087549612, 33.44018133063429,
    -117.61078592390551,units="kts") == 6936.687475706191,"SC KTS test"

def test_polar_distance_miles():
    assert pd.haversine(52.370216, 4.895168, 52.520008,
    13.404954,units="miles") == 587.6486318179826,"Unknown Miles test"
    assert pd.haversine(53.243518372219356, -0.4578422087549612, 33.44018133063429,
    -117.61078592390551,units="miles") == 7967.925567332664,"SC Miles test"
   
    #945793.4375088713

    #53.243518372219356, -0.4578422087549612
    #33.44018133063429, -117.61078592390551



