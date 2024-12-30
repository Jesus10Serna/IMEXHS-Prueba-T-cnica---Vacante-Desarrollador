export interface StainResult {
    id: number;
    imageUrl: string;
    totalPoints: number;
    pointsInside: number;
    estimatedArea: number;
    timestamp: Date;
    imageDimensions: {
      width: number;
      height: number;
    };
  }