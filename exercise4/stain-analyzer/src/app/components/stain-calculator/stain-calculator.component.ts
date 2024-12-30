import { Component, signal } from '@angular/core';
import { StainService } from '../../services/stain.service';
import { CommonModule } from '@angular/common';
import { MatTabsModule } from '@angular/material/tabs';
import { MatSliderModule } from '@angular/material/slider';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-stain-calculator',
  standalone: true,
  imports: [
    CommonModule,
    MatTabsModule,
    MatSliderModule,
    MatButtonModule,
    MatCardModule,
    FormsModule
  ],
  template: `
    <mat-card>
      <mat-card-content>
        <div class="flex flex-col gap-4">
          <!-- Image upload section -->
          <div class="upload-section">
            <input
              type="file"
              accept="image/*"
              (change)="onFileSelected($event)"
              class="hidden"
              #fileInput
            >
            <button 
              mat-raised-button 
              color="primary"
              (click)="fileInput.click()"
            >
              Upload Binary Image
            </button>
          </div>

          <!-- Preview section -->
          @if (imagePreview()) {
            <div class="preview-section">
              <img [src]="imagePreview()" alt="Preview" class="max-w-full h-auto">
            </div>
          }

          <!-- Controls section -->
          <div class="controls-section">
            <mat-slider
              min="100"
              max="10000"
              step="100"
              [disabled]="!imagePreview()"
              [(ngModel)]="pointCount"
            >
              <input matSliderThumb>
            </mat-slider>
            <span class="ml-2">Points: {{pointCount}}</span>
          </div>

          <!-- Calculate button -->
          <button 
            mat-raised-button 
            color="accent"
            [disabled]="!imagePreview()"
            (click)="calculateArea()"
          >
            Calculate Area
          </button>
        </div>
      </mat-card-content>
    </mat-card>
  `,
  styles: [`
    :host {
      display: block;
      max-width: 800px;
      margin: 0 auto;
    }
    .preview-section {
      margin: 1rem 0;
      border: 1px solid #ccc;
      padding: 1rem;
    }
  `]
})
export class StainCalculatorComponent {
  imagePreview = signal<string | null>(null);
  pointCount = 1000;
  private imageElement: HTMLImageElement | null = null;

  constructor(private stainService: StainService) {}

  onFileSelected(event: Event) {
    const file = (event.target as HTMLInputElement).files?.[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        const img = new Image();
        img.onload = () => {
          this.imageElement = img;
          this.imagePreview.set(img.src);
        };
        img.src = e.target?.result as string;
      };
      reader.readAsDataURL(file);
    }
  }

  calculateArea() {
    if (this.imageElement) {
      this.stainService.calculateStainArea(this.imageElement, this.pointCount);
    }
  }
}