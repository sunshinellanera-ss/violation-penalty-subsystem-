document.addEventListener('DOMContentLoaded', () => {

    // Modal functionality
    const modal = document.getElementById('violationModal');
    const openBtn = document.querySelector('.open-modal-btn');
    const closeBtn = document.querySelector('.close');

    openBtn.addEventListener('click', () => {
        modal.style.display = 'flex';

        // Reset modal fields
        document.getElementById("student_modal").value = '';
        document.getElementById("violation_modal").value = '';
        document.getElementById("offense_modal").value = '';
        document.getElementById("penalty_modal").value = '';
    });

    closeBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) modal.style.display = 'none';
    });

    // Auto Penalty & Offense Count
    const studentModal = document.getElementById("student_modal");
    const violationModalInput = document.getElementById("violation_modal");
    const offenseModal = document.getElementById("offense_modal");
    const penaltyModal = document.getElementById("penalty_modal");

    const violationRules = {
        "Dresscode": ["Memorize Mission-Vision", "Community Service", "Suspension"],
        "No Motor Sticker": ["Warning", "Parent Conference", "Suspension"],
        "Late Submission": ["Warning", "Extra Assignment", "Suspension"],
        "Absent without Leave": ["Warning", "Detention", "Suspension"]
    };

    let offenseCounts = {};

    function updatePenaltyModal() {
        const studentName = studentModal.value.trim();
        const violationType = violationModalInput.value;

        if (!studentName || !violationType) {
            offenseModal.value = '';
            penaltyModal.value = '';
            return;
        }

        const key = `${studentName}-${violationType}`;
        let count = offenseCounts[key] || 0;
        count += 1;
        offenseCounts[key] = count;

        offenseModal.value = count;
        const penalties = violationRules[violationType];
        penaltyModal.value = count <= penalties.length ? penalties[count-1] : penalties[penalties.length-1];
    }

    studentModal.addEventListener("input", () => {
        offenseModal.value = '';
        penaltyModal.value = '';
    });

    violationModalInput.addEventListener("change", updatePenaltyModal);

});

document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("viewModal");
    const closeBtn = modal.querySelector(".close");

    // View buttons
    const viewButtons = document.querySelectorAll(".view-btn");
    viewButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            // Populate modal with data attributes
            document.getElementById("modal-student").textContent = btn.dataset.student;
            document.getElementById("modal-course").textContent = btn.dataset.course;
            document.getElementById("modal-year").textContent = btn.dataset.year;
            document.getElementById("modal-violation").textContent = btn.dataset.violation;
            document.getElementById("modal-offense").textContent = btn.dataset.offense;
            document.getElementById("modal-penalty").textContent = btn.dataset.penalty;
            document.getElementById("modal-status").textContent = btn.dataset.status;
            document.getElementById("modal-officer").textContent = btn.dataset.officer;

            modal.style.display = "flex";
        });
    });

    // Close modal
    closeBtn.addEventListener("click", () => modal.style.display = "none");

    // Close on clicking outside modal content
    window.addEventListener("click", e => {
        if (e.target == modal) modal.style.display = "none";
    });
});