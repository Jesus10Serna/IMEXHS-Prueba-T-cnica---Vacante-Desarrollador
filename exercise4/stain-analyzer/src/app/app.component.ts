import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTabsModule } from '@angular/material/tabs';
import { StainCalculatorComponent } from './components/stain-calculator/stain-calculator.component';
import { ResultsTableComponent } from './components/results-table/results-table.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    CommonModule,
    MatTabsModule,
    StainCalculatorComponent,
    ResultsTableComponent
  ],
  template: `
    <div class="container mx-auto p-4">
      <h1 class="text-2xl font-bold mb-4">Stain Area Calculator</h1>
      
      <mat-tab-group>
        <!-- Calculator Tab -->
        <mat-tab label="Calculate Area">
          <div class="py-4">
            <app-stain-calculator></app-stain-calculator>
          </div>
        </mat-tab>
        
        <!-- Results Tab -->
        <mat-tab label="Previous Results">
          <div class="py-4">
            <app-results-table></app-results-table>
          </div>
        </mat-tab>
      </mat-tab-group>
    </div>
  `
})
export class AppComponent {}