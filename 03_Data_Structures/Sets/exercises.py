# ==============================================================================
# Module 03: Data Structures / Sets - Exercises
# ==============================================================================
# This file contains solved exercises to practice the concepts covered in the
# Sets submodule, focusing on mathematical operations and use cases.
# ==============================================================================

# ------------------------------------------------------------------------------
# EXERCISE 1: Combining Unique Attendees
# ------------------------------------------------------------------------------
# Description: You have two lists of attendees from two different sessions of an
#              event. Create a final, unique list of all attendees who came.
# This exercise demonstrates the use of set union.
# Source: Self-created

print("--- Exercise 1: Combining Unique Attendees ---")
morning_attendees = ["Alice", "Bob", "Charlie", "David"]
afternoon_attendees = ["Charlie", "Eve", "Frank", "Alice"]

print(f"Morning attendees: {morning_attendees}")
print(f"Afternoon attendees: {afternoon_attendees}")

# Convert lists to sets to easily find the union
set_morning = set(morning_attendees)
set_afternoon = set(afternoon_attendees)

# Find the union of both sets
all_unique_attendees_set = set_morning | set_afternoon

# Convert back to a list for the final result (if needed)
all_unique_attendees_list = sorted(list(all_unique_attendees_set)) # Sorted for consistent output

print(f"Final unique list of all attendees: {all_unique_attendees_list}")

# Expected Output:
# Morning attendees: ['Alice', 'Bob', 'Charlie', 'David']
# Afternoon attendees: ['Charlie', 'Eve', 'Frank', 'Alice']
# Final unique list of all attendees: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 2: Required Skills Check
# ------------------------------------------------------------------------------
# Description: A job requires a specific set of skills. A candidate has their
#              own list of skills. Check if the candidate has all the required skills.
# This demonstrates fast membership testing and the issubset() method.
# Source: Self-created

print("--- Exercise 2: Required Skills Check ---")
required_skills = {"Python", "Git", "SQL"}
candidate_skills_1 = {"Python", "Git", "SQL", "Docker", "JavaScript"}
candidate_skills_2 = {"Python", "HTML", "CSS"}

print(f"Required skills: {required_skills}")
print(f"Candidate 1 skills: {candidate_skills_1}")
print(f"Candidate 2 skills: {candidate_skills_2}")

# Check if the required skills are a subset of the candidate's skills
is_eligible_1 = required_skills.issubset(candidate_skills_1)
is_eligible_2 = required_skills.issubset(candidate_skills_2)

print(f"\nIs Candidate 1 eligible? {is_eligible_1}")
print(f"Is Candidate 2 eligible? {is_eligible_2}")


# Expected Output:
# Required skills: {'Python', 'Git', 'SQL'}
# Candidate 1 skills: {'Python', 'Git', 'SQL', 'Docker', 'JavaScript'}
# Candidate 2 skills: {'Python', 'HTML', 'CSS'}
#
# Is Candidate 1 eligible? True
# Is Candidate 2 eligible? False

print("-" * 40)


# ------------------------------------------------------------------------------
# EXERCISE 3: Finding Exclusive Features
# ------------------------------------------------------------------------------
# Description: You have a set of features for a "Premium" software version
#              and a set for the "Standard" version. Find the features that
#              are exclusive to the Premium version.
# This demonstrates the use of set difference.
# Source: Self-created

print("--- Exercise 3: Finding Exclusive Features ---")

standard_features = {"Basic editing", "File export", "Templates"}
premium_features = {"Basic editing", "File export", "Templates", "Cloud sync", "AI assistant"}

print(f"Standard features: {standard_features}")
print(f"Premium features: {premium_features}")

# Find the features that are in the premium set but not in the standard set
exclusive_to_premium = premium_features - standard_features

print(f"Features exclusive to Premium version: {exclusive_to_premium}")

# Expected Output:
# Standard features: {'Basic editing', 'Templates', 'File export'}
# Premium features: {'Basic editing', 'Templates', 'File export', 'Cloud sync', 'AI assistant'}
# Features exclusive to Premium version: {'Cloud sync', 'AI assistant'}

print("-" * 40)

# ==============================================================================
# End of Module 03/Sets Exercises
# ==============================================================================