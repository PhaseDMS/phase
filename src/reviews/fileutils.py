def review_comments_file_path(review, filename):
    """Rename document files on upload to match a custom filename."""
    from reviews.models import Review

    role_part = {
        Review.ROLES.reviewer: review.reviewer_id,
        Review.ROLES.leader: "leader",
        Review.ROLES.approver: "GTG",
    }

    return "reviews/{key}_{revision}_{role}_comments.{extension}".format(
        key=review.document.document_key,
        revision=review.revision_name,
        role=role_part[review.role],
        extension=filename.split(".")[-1],
    )


def dc_review_comments_file_path(revision, filename):
    return "reviews/{key}_{revision}_dc_comments.{extension}".format(
        key=revision.document.document_key,
        revision=revision.revision_name,
        extension=filename.split(".")[-1],
    )
