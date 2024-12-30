import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatTableModule } from '@angular/material/table';
import { StainService } from '../../services/stain.service';

@Component({
  selector: 'app-results-table',
  standalone: true,
  imports: [CommonModule, MatTableModule],
  template: `
    <table mat-table [dataSource]="stainService.stainResults()" class="w-full">
      <!-- Timestamp Column -->
      <ng-container matColumnDef="timestamp">
        <th mat-header-cell *matHeaderCellDef> Date </th>
        <td mat-cell *matCellDef="let element">
          {{element.timestamp | date:'short'}}
        </td>
      </ng-container>

      <!-- Points Column -->
      <ng-container matColumnDef="points">
        <th mat-header-cell *matHeaderCellDef> Points </th>
        <td mat-cell *matCellDef="let element">
          {{element.pointsInside}} / {{element.totalPoints}}
        </td>
      </ng-container>

      <!-- Area Column -->
      <ng-container matColumnDef="area">
        <th mat-header-cell *matHeaderCellDef> Estimated Area </th>
        <td mat-cell *matCellDef="let element">
          {{element.estimatedArea | number:'1.0-0'}} px²
        </td>
      </ng-container>

      <!-- Dimensions Column -->
      <ng-container matColumnDef="dimensions">
        <th mat-header-cell *matHeaderCellDef> Image Dimensions </th>
        <td mat-cell *matCellDef="let element">
          {{element.imageDimensions.width}} x {{element.imageDimensions.height}}
        </td>
      </ng-container>

      <tr mat-header-row *matHeaderRowDef="displayedColumns"></tr>
      <tr mat-row *matRowDef="let row; columns: displayedColumns;"></tr>
    </table>
  `
})
export class ResultsTableComponent {
  displayedColumns = ['timestamp', 'points', 'area', 'dimensions'];

  constructor(public stainService: StainService) {}
}