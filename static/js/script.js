// Load tasks from localStorage when the page loads
window.addEventListener('DOMContentLoaded', function() {
    loadTasks();
    
    // Add event listener to the add task button
    document.getElementById('addTaskButton').addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default form submission
        var taskName = document.getElementById('taskName').value;
        addTask(taskName);
        document.getElementById('taskForm').reset(); // Clear form field after adding task
    });
    
    // Add event listener for drag and drop
    var taskList = document.getElementById('taskList');
    var sortable = new Sortable(taskList, {
        animation: 150,
        onUpdate: function(event) {
            // Save tasks order and completion status to localStorage
            saveTasks();
        }
    });
});
    
// Function to load tasks from localStorage
function loadTasks() {
    var tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    tasks.forEach(function(task) {
        addTask(task.taskName, task.completed);
    });
    // Update progress bar
    updateProgressBar();
}

// Function to save tasks to localStorage
function saveTasks() {
    var taskItems = document.querySelectorAll('#taskList .list-group-item');
    var tasks = [];
    taskItems.forEach(function(item) {
        tasks.push({
            taskName: item.querySelector('.task-name').textContent,
            completed: item.classList.contains('list-group-item-success')
        });
    });
    localStorage.setItem('tasks', JSON.stringify(tasks));
    }
// Function to update progress bar
function updateProgressBar() {
    var totalTasks = document.querySelectorAll('#taskList .list-group-item').length;
    var completedTasks = document.querySelectorAll('#taskList .list-group-item-success').length;
    var progressPercentage = (completedTasks / totalTasks) * 100 || 0;
    var progressBar = document.getElementById('progressBar');
    progressBar.style.width = progressPercentage + '%';
    progressBar.textContent = progressPercentage.toFixed(0) + '%';
}  
    
// Function to add task to the list
function addTask(taskName, completed) {
    // Create list item element
    var listItem = document.createElement('li');
    listItem.className = 'list-group-item d-flex justify-content-between align-items-center';
    
    // Create span element for task name
    var taskNameSpan = document.createElement('span');
    taskNameSpan.textContent = taskName;
    taskNameSpan.className = 'task-name';
    listItem.appendChild(taskNameSpan);
    
    // Add delete button
    var deleteButton = document.createElement('button');
    deleteButton.className = 'btn btn-sm btn-danger delete-button';
    deleteButton.textContent = 'Delete';
    deleteButton.addEventListener('click', function(event) {
        event.stopPropagation(); // Prevent task item click event from firing
        // Remove the task item from the list
        listItem.remove();
        // Save tasks to localStorage
        saveTasks();
        // Update progress bar
        updateProgressBar();
    });
    listItem.appendChild(deleteButton);
    
    // Add click event listener to the task item
    listItem.addEventListener('click', function() {
        listItem.classList.toggle('list-group-item-success'); // Toggle 'completed' class
        // Save tasks to localStorage
        saveTasks();
        // Update progress bar
        updateProgressBar();
    });
    
    // Append list item to the task list
    document.getElementById('taskList').appendChild(listItem);        
    // Set completed status
    if (completed) {
    listItem.classList.add('list-group-item-success');
    }
    
    // Save tasks to localStorage
    saveTasks();
    // Update progress bar
    updateProgressBar();
}
    