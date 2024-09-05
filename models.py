from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

class SearchTerms(Base):
    __tablename__ = "search_terms"

    id = Column(Integer, primary_key=True, index=True)
    term = Column(String, index=True)
    generate_content = relationship("GenerateContent", back_populates="search_terms")
    sentiment_analysis = relationship("SentimentAnalysis", back_populates="search_terms")


class GeneratedContent(Base):
    __tablename__ = "generated_content"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    search_term_id = Column(Integer, ForeignKey("search_terms.id"))
    search_term = relationship("SearchTerm", back_populates="generated_content")



class SentimentAnalysis(Base):
    __tablename__ = "sentiment_analysis"

    id = Column(Integer, primary_key=True, index=True)
    readability = Column(String)
    sentiment = Column(String)
    search_term_id = Column(Integer, ForeignKey('search_terms.id'))
    search_term = relationship("SearchTerm", back_populates="sentiment_analysis")