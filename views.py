from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# View to display the grid
def grid_view(request):
    # Initialize a 10x10 grid in the session if not already set
    if 'grid' not in request.session:
        request.session['grid'] = [['' for _ in range(10)] for _ in range(10)]
    if 'styles' not in request.session:  # Initialize styles if not present
        request.session['styles'] = [['' for _ in range(10)] for _ in range(10)]
    
    return render(request, 'grid.html', {'grid': request.session['grid'], 'styles': request.session['styles']})


# View to handle cell updates
@csrf_exempt
def update_cell(request):
    if request.method == 'POST':
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))
        value = request.POST.get('value')

        # Get the current grid and styles from session
        grid = request.session.get('grid', [['' for _ in range(10)] for _ in range(10)])
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Update the cell's value
        grid[row][col] = value
        
        # Save updated grid and styles back to session
        request.session['grid'] = grid
        request.session['styles'] = styles
        
        return JsonResponse({'status': 'success'})


# View to handle adding rows
@csrf_exempt
def add_row(request):
    if request.method == 'POST':
        # Get current grid and styles from session
        grid = request.session.get('grid', [['' for _ in range(10)] for _ in range(10)])
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Add a new row (empty cells and styles)
        grid.append(['' for _ in range(len(grid[0]))])  # Preserve column length
        styles.append(['' for _ in range(len(styles[0]))])  # Preserve column styles
        request.session['grid'] = grid
        request.session['styles'] = styles
        
        return JsonResponse({'status': 'success', 'grid': grid})


# View to handle adding columns
@csrf_exempt
def add_column(request):
    if request.method == 'POST':
        # Get current grid and styles from session
        grid = request.session.get('grid', [['' for _ in range(10)] for _ in range(10)])
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Add a new column (empty cells and styles) to each row
        for row in grid:
            row.append('')
        for row in styles:
            row.append('')
        request.session['grid'] = grid
        request.session['styles'] = styles
        
        return JsonResponse({'status': 'success', 'grid': grid})


# View to handle deleting rows
@csrf_exempt
def delete_row(request):
    if request.method == 'POST':
        row = int(request.POST.get('row'))
        
        # Get current grid and styles from session
        grid = request.session.get('grid', [['' for _ in range(10)] for _ in range(10)])
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Ensure the row exists
        if 0 <= row < len(grid):
            grid.pop(row)  # Remove the row
            styles.pop(row)  # Remove the row styles
            request.session['grid'] = grid
            request.session['styles'] = styles
            return JsonResponse({'status': 'success', 'grid': grid})
        else:
            return JsonResponse({'status': 'error', 'message': 'Row not found'})


# View to handle deleting columns
@csrf_exempt
def delete_column(request):
    if request.method == 'POST':
        col = int(request.POST.get('col'))
        
        # Get current grid and styles from session
        grid = request.session.get('grid', [['' for _ in range(10)] for _ in range(10)])
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Ensure the column exists
        if 0 <= col < len(grid[0]):
            for row in grid:
                row.pop(col)  # Remove the column from each row
            for row in styles:
                row.pop(col)  # Remove the column styles
            request.session['grid'] = grid
            request.session['styles'] = styles
            return JsonResponse({'status': 'success', 'grid': grid})
        else:
            return JsonResponse({'status': 'error', 'message': 'Column not found'})


# View to handle bold formatting for a cell
@csrf_exempt
def toggle_bold(request):
    if request.method == 'POST':
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))
        
        # Get current styles from session
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Toggle the bold style for the selected cell
        current_style = styles[row][col]
        if 'bold' in current_style:
            styles[row][col] = current_style.replace('bold', '').strip()
        else:
            styles[row][col] = (current_style + ' bold').strip()

        request.session['styles'] = styles
        return JsonResponse({'status': 'success', 'styles': styles})


# View to handle italic formatting for a cell
@csrf_exempt
def toggle_italic(request):
    if request.method == 'POST':
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))
        
        # Get current styles from session
        styles = request.session.get('styles', [['' for _ in range(10)] for _ in range(10)])
        
        # Toggle the italic style for the selected cell
        current_style = styles[row][col]
        if 'italic' in current_style:
            styles[row][col] = current_style.replace('italic', '').strip()
        else:
            styles[row][col] = (current_style + ' italic').strip()

        request.session['styles'] = styles
        return JsonResponse({'status': 'success', 'styles': styles})
