def run_menu_choice(choice, tasks):
    if choice == "add":
        tasks.append("new task")
        return f"{len(tasks)} task(s)"
    elif choice == "clear":
        tasks.clear()
        return "0 task(s)"
    elif choice == "count":
        return f"{len(tasks)} task(s)"
    else:
        return "Unknown choice"
