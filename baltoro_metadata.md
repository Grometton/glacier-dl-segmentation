# Region Metadata: Baltoro Glacier

## Location
- Glacier: Baltoro Glacier
- Range: Karakoram, Pakistan
- Bounding Box:
  - Latitude: 35.55° to 35.78° N
  - Longitude: 76.19° to 76.60° E
- Approx. Area: ~400–500 km² (entire glacier and surroundings)

## Reason for Selection
- One of the longest glaciers outside the poles (~63 km)
- Visually distinctive: icefall zones, medial moraines, debris-covered ice
- Covered in multiple high-resolution Sentinel-2 scenes
- Included in RGI v6.0 (RGI60-14.01968)
- Useful for training glacier segmentation networks due to its complexity

## Target Use
- Deep learning-based glacier mask segmentation
- Training U-Net on multispectral inputs
- Testing model performance on rugged and debris-covered glaciers

## Known Challenges
- Frequent cloud cover; choose images from summer (July–Sept)
- Debris-covered ice can be hard to distinguish from surrounding rock




